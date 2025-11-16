# 🎯 Multi-Database Categorization Guide

## Complete Guide to Using the Categorized ETL Pipeline

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Why Categorization?](#why-categorization)
3. [Quick Start](#quick-start)
4. [Architecture](#architecture)
5. [Configuration](#configuration)
6. [Usage Examples](#usage-examples)
7. [API Reference](#api-reference)
8. [Migration Guide](#migration-guide)
9. [Best Practices](#best-practices)
10. [Troubleshooting](#troubleshooting)

---

## 🎯 Overview

The Multi-Database Categorization system automatically organizes your data into separate databases based on source category, with automatic versioning when schemas evolve.

### **Key Features**

✅ **Auto-Categorization** - AI detects data source from field names
✅ **Multi-Database Isolation** - Each source gets its own database
✅ **Automatic Versioning** - Schema changes create new versions
✅ **Retention Policies** - Different retention periods per source
✅ **Independent Evolution** - Schemas evolve independently
✅ **Cross-Version Queries** - Query data across all versions

---

## 💡 Why Categorization?

### **Without Categorization** ❌

```javascript
// Everything in ONE collection
hackathon_db.entries
├── {source: "ecommerce", product: "Laptop", price: 999}
├── {source: "hr", employee: "John", salary: 50000}
├── {source: "iot", temp: 25.5, sensor_id: "S001"}
└── {source: "api_logs", endpoint: "/api", status: 200}
```

**Problems:**
- No data isolation
- Schema conflicts ("price" means different things)
- Can't optimize indexes for all types
- No access control per source
- Compliance nightmare
- Must always filter by source

### **With Categorization** ✅

```javascript
// Organized by source and entity
ecommerce_db
  ├── products_v1       (initial schema)
  ├── products_v2       (evolved schema with currency field)
  └── orders_v1

hr_db
  ├── employees_v1
  └── employees_v2

iot_sensors_db
  ├── temperature_v1
  └── humidity_v1

api_logs_db
  └── logs_v1
```

**Benefits:**
- ✅ Complete data isolation
- ✅ Source-specific indexes
- ✅ Independent schema evolution
- ✅ Granular access control
- ✅ Different retention policies
- ✅ Better performance

---

## 🚀 Quick Start

### **1. Installation**

No new dependencies! Just use the existing setup:

```bash
pip install -r requirements.txt
```

### **2. Run with Categorization**

```bash
# Option 1: Use new categorized app
python app_categorized.py

# Option 2: Test migration first
python migrate_to_categorized.py --dry-run
```

### **3. Upload Data**

Visit `http://localhost:5001` and:
- Select data source (or use "Auto-Detect")
- Select entity type (or use "Auto-Detect")
- Upload your file
- See data organized into categorized databases!

---

## 🏗️ Architecture

### **Database Structure**

```
MongoDB Server
│
├── ecommerce_db
│   ├── products_v1          (schema version 1)
│   ├── products_v2          (schema version 2)
│   ├── orders_v1
│   └── _metadata
│       ├── schema_versions  (schema history)
│       ├── data_changes     (change tracking)
│       └── data_lineage     (lineage info)
│
├── hr_db
│   ├── employees_v1
│   ├── employees_v2
│   └── _metadata
│       └── ...
│
├── iot_sensors_db
│   ├── temperature_v1
│   └── _metadata
│       └── ...
│
└── pipeline_default
    └── (uncategorized data)
```

### **Collection Naming Convention**

```
{source}_{entity}_v{version}

Examples:
- ecommerce_products_v1
- ecommerce_products_v2
- hr_employees_v1
- api_logs_v1
```

---

## ⚙️ Configuration

### **Available Sources**

```python
SOURCE_DB_MAPPING = {
    "ecommerce": "ecommerce_db",
    "hr": "hr_db",
    "api_logs": "api_logs_db",
    "iot_sensors": "iot_sensors_db",
    "web_scraping": "web_scraping_db",
    "social_media": "social_media_db",
    "financial": "financial_db",
    "healthcare": "healthcare_db",
    "marketing": "marketing_db",
    "customer_data": "customer_data_db",
    "inventory": "inventory_db",
    "sales": "sales_db",
}
```

### **Retention Policies**

```python
RETENTION_POLICIES = {
    "ecommerce": 2555,      # 7 years
    "hr": 3650,             # 10 years
    "api_logs": 30,         # 30 days
    "iot_sensors": 90,      # 90 days
    "financial": 3650,      # 10 years
    "healthcare": 7300,     # 20 years
}
```

### **Auto-Categorization Rules**

The system detects sources based on field names:

```python
AUTO_CATEGORIZATION_RULES = {
    "ecommerce": ["price", "product", "sku", "cart", "order"],
    "hr": ["employee", "salary", "department", "hire_date"],
    "api_logs": ["endpoint", "status_code", "response_time"],
    "iot_sensors": ["temperature", "humidity", "sensor_id"],
}
```

---

## 📖 Usage Examples

### **Example 1: Upload E-Commerce Data**

```python
# Python code using the API
import requests

files = {'datafile': open('products.json', 'rb')}
data = {
    'source': 'ecommerce',  # or 'auto' for auto-detection
    'entity': 'products'     # or 'auto' for auto-detection
}

response = requests.post('http://localhost:5001/', files=files, data=data)
print(response.text)
```

**Result:**
```
✅ Loaded 100 records to ecommerce_db.ecommerce_products_v1
```

### **Example 2: Auto-Detection**

```python
# Upload without specifying source/entity
data = {'source': 'auto', 'entity': 'auto'}
files = {'datafile': open('data.json', 'rb')}

response = requests.post('http://localhost:5001/', files=files, data=data)
```

AI analyzes fields like `["product", "price", "sku"]` and automatically:
- Detects source: `ecommerce`
- Detects entity: `products`
- Routes to: `ecommerce_db.ecommerce_products_v1`

### **Example 3: Schema Evolution**

```python
# First upload - creates v1
data_v1 = [
    {"id": 1, "product": "Laptop", "price": 999}
]
# → ecommerce_products_v1

# Second upload with new field - creates v2
data_v2 = [
    {"id": 2, "product": "Mouse", "price": 29, "currency": "USD"}
]
# → ecommerce_products_v2 (new version!)
```

### **Example 4: Query Specific Version**

```python
import requests

response = requests.post('http://localhost:5001/api/v2/query', json={
    "source": "ecommerce",
    "entity": "products",
    "version": 1,  # Query v1 specifically
    "query": {"price": {"$lt": 100}},
    "limit": 10
})

data = response.json()
print(f"Found {data['count']} records")
```

### **Example 5: Query Across All Versions**

```python
response = requests.post('http://localhost:5001/api/v2/query/across_versions', json={
    "source": "ecommerce",
    "entity": "products",
    "query": {"price": {"$lt": 100}},
    "limit": 100
})

data = response.json()
print(f"Found {data['total_count']} records across all versions")
```

### **Example 6: Get Schema History**

```python
response = requests.get('http://localhost:5001/api/v2/schema/history', params={
    "source": "ecommerce",
    "entity": "products"
})

history = response.json()['history']
for version in history:
    print(f"Version {version['version']}: {len(version['schema'])} fields")
    if version['changes']:
        print(f"  Added: {version['changes']['added_fields']}")
        print(f"  Removed: {version['changes']['removed_fields']}")
```

---

## 🔌 API Reference

### **Base URL:** `http://localhost:5001/api/v2`

### **Endpoints**

#### **GET /health**
Check API health

**Response:**
```json
{
  "status": "healthy",
  "service": "categorized-etl-pipeline",
  "version": "2.0.0"
}
```

#### **GET /sources**
List available data sources

**Response:**
```json
{
  "status": "success",
  "sources": ["ecommerce", "hr", "api_logs", ...],
  "count": 12
}
```

#### **GET /databases/stats**
Get statistics across all databases

**Response:**
```json
{
  "status": "success",
  "data": {
    "databases": {
      "ecommerce": {"collections": 3, "records": 1500},
      "hr": {"collections": 2, "records": 250}
    },
    "total_records": 1750,
    "total_collections": 5
  }
}
```

#### **GET /schema/history?source=X&entity=Y**
Get schema evolution history

**Parameters:**
- `source` - Data source category
- `entity` - Entity type

**Response:**
```json
{
  "status": "success",
  "source": "ecommerce",
  "entity": "products",
  "version_count": 2,
  "history": [
    {
      "version": 1,
      "schema": {...},
      "created_at": "2025-11-15T10:00:00",
      "changes": null
    },
    {
      "version": 2,
      "schema": {...},
      "created_at": "2025-11-15T11:00:00",
      "changes": {
        "added_fields": ["currency"],
        "removed_fields": [],
        "modified_fields": []
      }
    }
  ]
}
```

#### **POST /query**
Query data from specific source/entity/version

**Request Body:**
```json
{
  "source": "ecommerce",
  "entity": "products",
  "version": 1,  // optional, defaults to latest
  "query": {"price": {"$lt": 100}},
  "limit": 50
}
```

**Response:**
```json
{
  "status": "success",
  "source": "ecommerce",
  "entity": "products",
  "version": 1,
  "count": 10,
  "data": [...]
}
```

#### **POST /query/across_versions**
Query across all schema versions

**Request Body:**
```json
{
  "source": "ecommerce",
  "entity": "products",
  "query": {"price": {"$lt": 100}},
  "limit": 100
}
```

#### **POST /auto_categorize**
Auto-detect source and entity from sample

**Request Body:**
```json
{
  "sample_record": {
    "product": "Laptop",
    "price": 999,
    "sku": "LAP-001"
  }
}
```

**Response:**
```json
{
  "status": "success",
  "detected": {
    "source": "ecommerce",
    "entity": "products",
    "database": "ecommerce_db"
  },
  "sample_fields": ["product", "price", "sku"]
}
```

---

## 🔄 Migration Guide

### **Migrate Existing Data**

If you have data in the old single-database structure, use the migration script:

#### **Step 1: Dry Run (See What Would Happen)**

```bash
python migrate_to_categorized.py --dry-run
```

Output:
```
Migration Plan:
  Source Category: ecommerce
  Entity Type: products
  Total Records: 1000
  Target Database: ecommerce_db
  Mode: DRY RUN

⚠️ DRY RUN MODE - No data will be modified
Would migrate 1000 records to:
  Database: ecommerce_db
  Collection Pattern: ecommerce_products_v*
```

#### **Step 2: Run Migration**

```bash
python migrate_to_categorized.py
```

You'll be prompted to confirm:
```
Proceed with migration? (yes/no): yes
```

Output:
```
Starting migration...
Migrating: 100%|██████████| 1000/1000 [00:05<00:00, 200records/s]

MIGRATION COMPLETE
Total Records: 1000
Successfully Migrated: 1000
Errors: 0
Duration: 5.00 seconds
Speed: 200.00 records/second
```

#### **Step 3: Manual Categorization (Optional)**

```bash
python migrate_to_categorized.py --source hr --entity employees
```

#### **Options:**

```bash
--dry-run           # Show plan without executing
--source SOURCE     # Manually specify source
--entity ENTITY     # Manually specify entity
--batch-size N      # Batch size (default: 1000)
```

---

## 💡 Best Practices

### **1. Choose Appropriate Sources**

Use specific sources for better organization:
- ✅ Use `ecommerce` for product data
- ✅ Use `hr` for employee data
- ✅ Use `api_logs` for API logs
- ❌ Don't use `auto` for production (be explicit)

### **2. Name Entities Clearly**

Good entity names:
- ✅ `products`, `orders`, `employees`, `customers`
- ❌ `data`, `stuff`, `records`

### **3. Monitor Schema Evolution**

```python
# Check schema history regularly
history = loader.get_schema_history("ecommerce", "products")
print(f"Total versions: {len(history)}")
```

### **4. Set Appropriate Retention Policies**

Edit `config_categorized.py` to match your needs:
```python
RETENTION_POLICIES = {
    "api_logs": 30,        # Logs only need 30 days
    "financial": 3650,     # Financial data: 10 years
    "customer_data": 1825, # Customer data: 5 years (GDPR)
}
```

### **5. Use Cross-Version Queries Wisely**

Cross-version queries can be slow. Use when:
- ✅ Need historical analysis
- ✅ Migration/reconciliation
- ❌ Regular application queries (use specific version)

---

## 🐛 Troubleshooting

### **Problem: Data Not Auto-Categorized**

**Solution:**
```python
# Check auto-categorization rules
from config_categorized import DatabaseConfig

fields = ["your", "field", "names"]
detected = DatabaseConfig.detect_source_from_fields(fields)
print(f"Detected source: {detected}")
```

If detection fails, manually specify source:
```python
data = {'source': 'ecommerce', 'entity': 'products'}
```

### **Problem: Too Many Schema Versions**

**Cause:** Small schema changes creating new versions

**Solution:**
1. Batch similar uploads together
2. Normalize data before upload
3. Use consistent field names

### **Problem: Can't Find Data**

**Solution:**
```python
# Check database stats
import requests
response = requests.get('http://localhost:5001/api/v2/databases/stats')
print(response.json())

# Check schema history
response = requests.get('http://localhost:5001/api/v2/schema/history',
                       params={"source": "ecommerce", "entity": "products"})
print(response.json())
```

### **Problem: Retention Policy Deleting Data**

**Solution:**
```python
# Check retention policy
response = requests.get('http://localhost:5001/api/v2/retention_policy',
                       params={"source": "ecommerce"})
print(f"Retention: {response.json()['retention_days']} days")

# Adjust in config_categorized.py
RETENTION_POLICIES = {
    "ecommerce": 3650,  # Increase to 10 years
}
```

---

## 📊 Monitoring

### **Check Database Stats**

```bash
curl http://localhost:5001/api/v2/databases/stats
```

### **Monitor Schema Evolution**

```bash
curl "http://localhost:5001/api/v2/schema/history?source=ecommerce&entity=products"
```

### **Track Changes**

```bash
curl "http://localhost:5001/api/v2/changes?source=ecommerce&entity=products&limit=10"
```

---

## 🎓 Advanced Topics

### **Custom Source Categories**

Edit `config_categorized.py`:

```python
SOURCE_DB_MAPPING = {
    # ... existing sources ...
    "my_custom_source": "my_custom_db",
}

AUTO_CATEGORIZATION_RULES = {
    # ... existing rules ...
    "my_custom_source": ["custom_field1", "custom_field2"],
}

RETENTION_POLICIES = {
    # ... existing policies ...
    "my_custom_source": 365,  # 1 year
}
```

### **Programmatic Usage**

```python
from load_categorized import CategorizedDataLoader
from config_categorized import DatabaseConfig

# Initialize loader
loader = CategorizedDataLoader(DatabaseConfig())

# Load data
result = loader.load_categorized_data(
    batch=[{"product": "Laptop", "price": 999}],
    source="ecommerce",
    entity="products",
    schema={"product": {"type": "string"}, "price": {"type": "float"}}
)

print(f"Loaded {result['inserted_count']} records to version {result['version']}")

# Query data
results = loader.query_across_versions("ecommerce", "products", {})
print(f"Found {len(results)} records across all versions")

# Get schema history
history = loader.get_schema_history("ecommerce", "products")
print(f"Schema has {len(history)} versions")

# Close connection
loader.close()
```

---

## 📞 Support

For issues or questions:
- Check logs: `logs/etl.log`
- Run tests: `python test_categorized.py`
- Review examples above
- Check MongoDB directly: `mongo` → `show dbs` → `use ecommerce_db` → `show collections`

---

**Built with ❤️ for Enterprise-Grade Data Management** 🚀
