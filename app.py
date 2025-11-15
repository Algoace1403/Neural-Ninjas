from flask import Flask, render_template, request
import logging
from datetime import datetime
from bson import ObjectId
from extract import extract_data, batch_data
from transform import infer_schema, transform_batch
from load import load_data, save_schema_version
from config import BATCH_SIZE

app = Flask(__name__)

def sanitize_for_json(data):
    """Remove or convert MongoDB ObjectId and datetime fields for JSON serialization"""
    if isinstance(data, list):
        return [sanitize_for_json(item) for item in data]
    elif isinstance(data, dict):
        sanitized = {}
        for key, value in data.items():
            if key == '_id':
                # Skip _id field entirely
                continue
            elif isinstance(value, ObjectId):
                # Convert ObjectId to string
                sanitized[key] = str(value)
            elif isinstance(value, datetime):
                # Convert datetime to ISO format string
                sanitized[key] = value.isoformat()
            elif isinstance(value, dict):
                sanitized[key] = sanitize_for_json(value)
            elif isinstance(value, list):
                sanitized[key] = sanitize_for_json(value)
            else:
                sanitized[key] = value
        return sanitized
    elif isinstance(data, datetime):
        return data.isoformat()
    elif isinstance(data, ObjectId):
        return str(data)
    else:
        return data

logging.basicConfig(filename='logs/etl.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

@app.route("/", methods=["GET", "POST"])
def index():
    schema = {}
    transformed = []
    msg = ""
    stats = {}
    all_changes = []
    schema_version = None

    if request.method == "POST":
        file = request.files["datafile"]
        data = extract_data(file)
        if not data:
            msg = "Invalid file format. Please upload JSON or CSV with records."
        else:
            total_duplicates = 0
            for batch in batch_data(data, BATCH_SIZE):
                schema = infer_schema(batch, schema)
                t_batch = transform_batch(batch, schema)
                changes, dup_count = load_data(t_batch)
                total_duplicates += dup_count
                if changes:
                    all_changes.extend(changes)
                transformed = t_batch[:5]  # show sample of uploaded batch

            # Calculate statistics
            stats = {
                'total_records': len(data),
                'total_fields': len(schema),
                'fields_by_type': {},
                'changes_detected': len(all_changes),
                'duplicates_removed': total_duplicates,
                'inserted_records': len(data) - total_duplicates
            }

            # Count fields by type
            for field_name, field_info in schema.items():
                field_type = field_info.get('type', 'unknown')
                stats['fields_by_type'][field_type] = stats['fields_by_type'].get(field_type, 0) + 1

            # Save schema version
            schema_version = save_schema_version(schema, stats)

            change_msg = f" | {len(all_changes)} changes detected" if all_changes else ""
            dup_msg = f" | {total_duplicates} duplicates skipped" if total_duplicates > 0 else ""
            msg = f"✓ Processed {len(data)} records, inserted {stats['inserted_records']} with {len(schema)} fields! Schema v{schema_version} saved.{change_msg}{dup_msg}"

    # Sanitize data for JSON serialization (remove MongoDB ObjectId)
    transformed_clean = sanitize_for_json(transformed)
    changes_clean = sanitize_for_json(all_changes)

    return render_template("index.html", schema=schema, transformed=transformed_clean, msg=msg, stats=stats, changes=changes_clean, schema_version=schema_version)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
