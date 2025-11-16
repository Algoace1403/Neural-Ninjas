# 📁 Supported File Formats

Your Dynamic ETL Pipeline now supports **4 file formats** with intelligent data extraction:

---

## 1. 📋 JSON Files (.json)

**Standard JSON array format**

### Example:
```json
[
  {"product": "Laptop", "price": 999, "category": "Electronics"},
  {"product": "Mouse", "price": 29, "category": "Electronics"}
]
```

### Features:
- ✅ Nested objects supported
- ✅ Arrays and complex structures
- ✅ Automatic type detection
- ✅ Full schema inference

---

## 2. 📊 CSV Files (.csv)

**Comma-separated values with headers**

### Example:
```csv
product,price,category,stock
Laptop,999,Electronics,50
Mouse,29,Electronics,150
```

### Features:
- ✅ Header row detection
- ✅ Automatic type conversion
- ✅ Handles quoted values
- ✅ UTF-8 encoding support

---

## 3. 📄 PDF Files (.pdf)

**Comprehensive PDF data extraction**

### Supported PDF Types:
1. **Tables** - Extracts tabular data from PDFs
2. **Text** - Page-by-page text extraction
3. **Structured Data** - Pattern-based extraction
4. **Invoices** - Invoice-specific parsing
5. **Resumes** - Resume data extraction

### Example Use Cases:
- Bank statements
- Invoices and receipts
- Reports with tables
- Forms and documents
- Resumes/CVs

### Features:
- ✅ Multi-method extraction (pdfplumber + tabula-py)
- ✅ Table detection and parsing
- ✅ Pattern recognition (emails, phones, dates, amounts)
- ✅ Fallback strategies for complex PDFs
- ✅ Automatic mode selection

### Dependencies:
```bash
pip install PyPDF2 pdfplumber tabula-py pandas
```

---

## 4. 📝 TXT Files (.txt)

**Intelligent text file parsing with auto-detection**

### Supported TXT Formats:

#### A. **JSON Lines (.jsonl format)**
One JSON object per line
```txt
{"product": "Laptop", "price": 999}
{"product": "Mouse", "price": 29}
```

#### B. **Key-Value Pairs**
```txt
name: John Doe
email: john@example.com
age: 30

name: Jane Smith
email: jane@example.com
age: 28
```

Supports both formats:
- `key: value`
- `key=value`
- `key = value`

#### C. **Tabular Data**
Tab or space-separated values
```txt
name          age    department
John Doe      30     Engineering
Jane Smith    28     Marketing
```

#### D. **Log Files**
```txt
2025-11-15 10:15:23 INFO Server started successfully
2025-11-15 10:16:45 ERROR Database connection failed
2025-11-15 10:17:12 WARNING High memory usage detected
```

Supports multiple log formats:
- Apache/Nginx style
- Python logging format
- Custom timestamp formats

#### E. **Line Records**
Each line becomes a record with automatic pattern extraction
```txt
Contact: john@example.com, Phone: 555-123-4567
Order #12345, Date: 2025-11-15, Amount: $99.99
```

Auto-extracts:
- Emails
- Phone numbers
- Dates
- Numbers/amounts

### TXT Features:
- ✅ **Auto-detection** - Automatically identifies format
- ✅ **Type conversion** - Converts strings to int/float/bool
- ✅ **Pattern extraction** - Finds emails, phones, dates
- ✅ **Multi-format support** - Handles 6+ different formats
- ✅ **Intelligent parsing** - Falls back gracefully
- ✅ **Empty line handling** - Uses as record separators
- ✅ **Header detection** - Identifies header rows in tabular data

---

## 🧪 Sample Files

Sample files for testing are available in `/tmp/`:

1. **Key-Value Format**: `/tmp/test_sample.txt`
   - Employee records with name, email, age, department, salary

2. **Log Format**: `/tmp/sample_log.txt`
   - Server logs with timestamps and levels

3. **JSON Lines**: `/tmp/sample_jsonlines.txt`
   - Product catalog data

---

## 🚀 Usage

### Via Web Interface:
1. Go to **http://localhost:5001**
2. Select file (JSON, CSV, PDF, or TXT)
3. Choose categorization (Auto-Detect recommended)
4. Upload and process

### File Selection:
The file input now accepts:
```html
<input type="file" accept=".json,.csv,.pdf,.txt">
```

---

## 📊 Processing Flow

```
Upload File
    ↓
Auto-detect Format
    ↓
Extract Data (JSON/CSV/PDF/TXT)
    ↓
Infer Schema
    ↓
Transform Data
    ↓
Auto-categorize (AI)
    ↓
Load to Appropriate Database
    ↓
Version & Track Changes
```

---

## 🎯 Format Detection Logic

### TXT Auto-Detection:
1. Check for JSON objects → JSON Lines
2. Check for log patterns → Log File
3. Check for key:value pairs → Key-Value
4. Check for tabs/multiple spaces → Tabular
5. Default → Line Records

### PDF Auto-Detection:
1. Try table extraction first
2. If tables found → Use table data
3. If no tables → Extract structured patterns
4. Fallback → Text extraction

---

## 💡 Best Practices

### For TXT Files:
1. **Use consistent formatting** - Same format throughout file
2. **Empty lines as separators** - For key-value pairs
3. **Include headers** - For tabular data
4. **Structured logs** - Use standard log formats

### For PDF Files:
1. **Clear tables** - Well-defined borders
2. **Text-based PDFs** - Not scanned images
3. **Consistent formatting** - Regular structure

### For All Files:
1. **UTF-8 encoding** - Ensures compatibility
2. **Valid data** - Clean, well-formatted
3. **Reasonable size** - Under 50MB recommended

---

## 🔧 Advanced Options

### Manual Format Selection:
You can specify the extraction mode in code:

```python
# For TXT files
from txt_extractor import extract_data_from_txt
data = extract_data_from_txt(file, mode='key_value')
# Modes: 'auto', 'key_value', 'tabular', 'line_records', 'json_lines', 'log_file'

# For PDF files
from pdf_extractor import extract_data_from_pdf
data = extract_data_from_pdf(file, mode='tables')
# Modes: 'auto', 'tables', 'text', 'structured', 'invoices', 'resumes'
```

---

## 📈 Examples by Domain

### E-Commerce (CSV/JSON/TXT):
```csv
product,price,sku,stock
Laptop,999,LAP-001,50
```

### HR Data (TXT Key-Value):
```txt
employee: John Doe
salary: 75000
department: Engineering
```

### Server Logs (TXT Log Format):
```txt
2025-11-15 10:15:23 INFO User login successful
```

### Invoices (PDF):
- Upload invoice PDF
- Extracts: date, invoice number, items, amounts, totals

### Sensor Data (JSON Lines .txt):
```txt
{"sensor_id": "S001", "temperature": 25.5, "timestamp": "2025-11-15T10:00:00"}
```

---

## ✅ Summary

| Format | Extension | Auto-Extract | AI Categorize | Schema Version |
|--------|-----------|--------------|---------------|----------------|
| JSON   | .json     | ✅           | ✅            | ✅             |
| CSV    | .csv      | ✅           | ✅            | ✅             |
| PDF    | .pdf      | ✅           | ✅            | ✅             |
| TXT    | .txt      | ✅           | ✅            | ✅             |

**All formats support:**
- ✅ Automatic data extraction
- ✅ AI-powered categorization
- ✅ Schema detection and versioning
- ✅ Multi-database routing
- ✅ Duplicate detection
- ✅ Change tracking

---

## 🎉 You're Ready!

Upload any of these file types at **http://localhost:5001** and watch the AI automatically:
1. Extract structured data
2. Detect the domain/category
3. Route to appropriate database
4. Version the schema
5. Track changes

**Try it now!** 🚀
