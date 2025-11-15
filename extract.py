import json
import csv

def extract_data(file_storage):
    """Extract data from uploaded file (JSON or CSV)."""
    filename = file_storage.filename
    if filename.endswith(".json"):
        data = json.load(file_storage)
    elif filename.endswith(".csv"):
        file_storage.stream.seek(0)
        reader = csv.DictReader(file_storage.stream.read().decode("utf-8").splitlines())
        data = list(reader)
    else:
        # Unsupported type
        data = []
    return data

def batch_data(data, batch_size):
    """Yield data in batches for scalability."""
    batch = []
    for record in data:
        batch.append(record)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch