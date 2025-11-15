# 🚀 Dynamic ETL Pipeline - AI Powered

Upload any JSON/CSV file. The pipeline automatically infers schema with **AI type detection**, cleans every record, **detects changes**, removes duplicates, and loads everything into MongoDB with full versioning!

## ✨ Key Features

### 🤖 AI-Powered Intelligence
- **Smart Type Detection**: Automatically detects integers, floats, emails, dates, URLs, booleans
- **Schema Evolution**: Schema adapts as new fields appear
- **Data Normalization**: Standardizes dates, emails, numbers automatically

### 🔍 Advanced Tracking
- **Schema Versioning**: Every unique schema saved with timestamps
- **Change Detection**: Tracks changes in key fields (price, discount, score, etc.)
- **Deduplication**: Automatically prevents duplicate records
- **Full Audit Trail**: Complete history in MongoDB

### 💎 Production Ready
- **Batch Processing**: Handles large datasets efficiently
- **Error Handling**: Robust error management
- **Comprehensive Logging**: All operations logged with timestamps
- **Beautiful UI**: Modern dashboard with real-time statistics

## 🎯 How To Run

### Prerequisites
- Python 3.7+
- MongoDB running locally or connection URI

### Installation
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Start MongoDB (if not running)
mongod
# OR use MongoDB Compass

# 3. Run the application
python app.py

# 4. Open browser
http://127.0.0.1:5000
```

## 📊 Testing the Features

### Test 1: Type Detection
1. Upload `test_data_complete.json`
2. See AI-detected types: integer, float, email, date, url, boolean
3. Check MongoDB Compass → `schema_versions` collection

### Test 2: Deduplication
1. Upload `test_data_complete.json`
2. Upload the same file again
3. Notice "X duplicates skipped" message

### Test 3: Change Detection
1. Upload `test_data_complete.json`
2. Upload `test_data_modified.json` (has changed prices/scores)
3. See changes table showing old vs new values
4. Check MongoDB → `data_changes` collection

### Test 4: Schema Evolution
1. Upload `sample.json` (different structure)
2. Upload `test_data_complete.json` (different fields)
3. See schema version increment (v1 → v2)

## 📁 MongoDB Collections

The system creates 3 collections:

1. **`entries`** - Main data storage with metadata
2. **`schema_versions`** - Schema history and versions
3. **`data_changes`** - Field change tracking

## 🎨 What Makes This Special?

✅ **Zero Configuration** - No manual schema definition needed
✅ **Intelligent** - AI-powered type inference
✅ **Adaptive** - Handles evolving data structures
✅ **Smart** - Automatic deduplication
✅ **Tracking** - Full change detection and history
✅ **Production-Grade** - Error handling, logging, batch processing
✅ **Beautiful UI** - Modern dashboard with statistics

## 🔧 Configuration

Edit `config.py` to customize:
- MongoDB connection URI
- Database and collection names
- Batch processing size

## 📈 Use Cases

Perfect for:
- 🛒 E-commerce price/product tracking
- 📊 Multi-source data aggregation
- 🌐 Web scraping pipelines
- 📡 API data collection
- 🔄 Real-time data synchronization

## 🚀 Future Enhancements

See `FEATURES.md` for:
- Detailed feature documentation
- What's implemented vs vision
- Hackathon demo script
- Enhancement roadmap

## 📝 Tech Stack

- **Backend**: Flask, Python 3
- **Database**: MongoDB
- **Processing**: Batch processing with configurable size
- **Type Detection**: Regex + intelligent inference
- **UI**: HTML5, CSS3, Jinja2 templates

---

**Built for Hackathon** | Scalable | Production-Ready | AI-Powered 🤖
