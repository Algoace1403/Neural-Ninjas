# 🚀 Quick Start - Run on Localhost

## ⚡ **FASTEST WAY (30 seconds)**

### **Step 1: Open Terminal**
```bash
cd "/Users/aks/Downloads/pipeline (1)"
```

### **Step 2: Run the startup script**
```bash
./start_localhost.sh
```

**That's it!** The script will:
- ✅ Check Python
- ✅ Check MongoDB
- ✅ Check/Install Ollama (for AI)
- ✅ Install dependencies
- ✅ Start the app

---

## 📍 **Access the Website**

Once started, open your browser and go to:

### **Main Application (Multi-Database AI)**
```
http://localhost:5001
```

### **Analytics Dashboard**
```
http://localhost:8050
```

---

## 🔧 **Manual Setup (If Script Doesn't Work)**

### **1. Install Prerequisites**

#### **A. Install MongoDB**
```bash
# macOS
brew install mongodb-community

# Start MongoDB
brew services start mongodb-community

# OR download from: https://www.mongodb.com/try/download/community
```

#### **B. Install Ollama (for AI features)**
```bash
# macOS
brew install ollama

# OR download from: https://ollama.ai

# Start Ollama
ollama serve

# Pull the AI model (in another terminal)
ollama pull llama2
```

#### **C. Install Python Dependencies**
```bash
cd "/Users/aks/Downloads/pipeline (1)"
pip install -r requirements.txt
```

### **2. Start the Application**

**Option A: Multi-Database Categorized App (RECOMMENDED)**
```bash
python app_categorized.py
```
Visit: `http://localhost:5001`

**Option B: Original App**
```bash
python app.py
```
Visit: `http://localhost:5001`

**Option C: Analytics Dashboard**
```bash
python dashboard.py
```
Visit: `http://localhost:8050`

---

## 🎯 **What You'll See**

### **Homepage Features:**
- 📤 **File Upload** - Upload JSON, CSV, or PDF files
- 🤖 **Auto-Detection** - AI automatically categorizes your data
- 🗄️ **Multi-Database** - Data organized into separate databases
- 📊 **Schema Versioning** - Automatic version tracking
- 📈 **Real-time Stats** - See processing results instantly

### **AI Features (with Ollama):**
- 🧠 Universal data type detection
- 🏷️ Automatic categorization (ANY domain, not just predefined)
- 💬 Natural language queries
- 🔗 Relationship detection
- 📝 Data quality reports

---

## 🧪 **Test It Out**

### **Upload Sample Data:**

**1. E-Commerce Data (sample.json)**
```json
[
  {"product": "Laptop", "price": 999, "sku": "LAP-001"},
  {"product": "Mouse", "price": 29, "sku": "MOU-001"}
]
```

**2. HR Data**
```json
[
  {"employee": "John Doe", "salary": 50000, "department": "Engineering"},
  {"employee": "Jane Smith", "salary": 60000, "department": "Marketing"}
]
```

**3. IoT Sensor Data**
```json
[
  {"sensor_id": "S001", "temperature": 25.5, "humidity": 60},
  {"sensor_id": "S002", "temperature": 26.0, "humidity": 58}
]
```

### **Watch the Magic:**
- AI detects the domain automatically
- Data goes to appropriate database
- Schema is versioned
- Changes are tracked

---

## 🐛 **Troubleshooting**

### **Problem: Port 5001 already in use**
**Solution:**
```bash
# Kill process on port 5001
lsof -ti:5001 | xargs kill -9

# OR change port in app
python app_categorized.py --port 5002
```

### **Problem: MongoDB not connecting**
**Solution:**
```bash
# Check if MongoDB is running
pgrep mongod

# If not, start it
mongod

# OR use MongoDB Compass (GUI)
```

### **Problem: Ollama not working**
**Solution:**
```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

# If not, start it
ollama serve

# Pull model
ollama pull llama2

# The app works WITHOUT Ollama (AI features disabled)
```

### **Problem: Dependencies not installing**
**Solution:**
```bash
# Upgrade pip first
pip install --upgrade pip

# Install dependencies one by one
pip install flask flask-cors pymongo pandas numpy scikit-learn

# For AI features
pip install transformers torch sentence-transformers
```

---

## 📱 **Access from Other Devices**

### **Access from Phone/Tablet on Same Network:**

1. Find your computer's IP address:
```bash
# macOS/Linux
ifconfig | grep "inet "

# Look for something like: 192.168.1.XXX
```

2. On your phone/tablet browser, visit:
```
http://192.168.1.XXX:5001
```
(Replace XXX with your IP)

---

## ⚙️ **Advanced Options**

### **Run with Custom Settings:**

```bash
# Use different MongoDB
export MONGO_URI="mongodb://your-server:27017/"
python app_categorized.py

# Disable AI features
export USE_LLM=false
python app_categorized.py

# Change port
python app_categorized.py --port 8080
```

### **Run in Background:**

```bash
# Start in background
nohup python app_categorized.py > app.log 2>&1 &

# Check logs
tail -f app.log

# Stop
pkill -f app_categorized.py
```

---

## 📊 **API Testing**

### **Test API with curl:**

```bash
# Health check
curl http://localhost:5001/api/v2/health

# Get available sources
curl http://localhost:5001/api/v2/sources

# Get database stats
curl http://localhost:5001/api/v2/databases/stats

# Auto-categorize sample data
curl -X POST http://localhost:5001/api/v2/auto_categorize \
  -H "Content-Type: application/json" \
  -d '{"sample_record": {"product": "Laptop", "price": 999}}'
```

---

## 🎥 **Quick Demo Flow**

1. **Start the app:**
   ```bash
   ./start_localhost.sh
   ```

2. **Open browser:** `http://localhost:5001`

3. **Select:**
   - Source: 🤖 Auto-Detect
   - Entity: 🤖 Auto-Detect

4. **Upload:** `test_data_complete.json` or any JSON/CSV file

5. **See results:**
   - ✅ Data categorized automatically
   - ✅ Schema detected with AI
   - ✅ Database created
   - ✅ Version tracked

6. **Check MongoDB:**
   ```bash
   mongo
   > show dbs
   > use ecommerce_db
   > show collections
   > db.ecommerce_products_v1.find().pretty()
   ```

---

## 🌟 **Features to Try**

### **1. Auto-Categorization**
Upload ANY type of data and watch AI detect:
- Domain (ecommerce, healthcare, finance, etc.)
- Entity type (products, patients, transactions, etc.)
- Appropriate database

### **2. Schema Versioning**
Upload same data with new fields:
- First upload → v1
- Second upload (with new field) → v2
- Query across versions

### **3. Natural Language Queries** (with Ollama)
Coming soon in UI!

### **4. Data Quality Reports**
See completeness, anomalies, recommendations

---

## 📞 **Need Help?**

### **Check Logs:**
```bash
# App logs
tail -f logs/etl.log

# Ollama logs
tail -f /tmp/ollama.log

# MongoDB logs
tail -f /tmp/mongodb.log
```

### **Run Tests:**
```bash
# Test categorization
python test_categorized.py

# Test Ollama integration
python -c "from ollama_integration import get_ollama_client; print(get_ollama_client().list_models())"
```

---

## ✅ **You're Ready!**

The app is running at: **http://localhost:5001**

**Try it now!** 🚀

---

**Quick Links:**
- 📖 Full Guide: `CATEGORIZATION_GUIDE.md`
- 🧪 Tests: `python test_categorized.py`
- 🔧 Config: `config_categorized.py`
- 📊 API Docs: `api_categorized.py`
