# 📄 PDF Data Extraction Guide

## Overview

The AI-powered pipeline now supports **comprehensive PDF data extraction**, including:
- ✅ Tables from PDFs
- ✅ Text content extraction
- ✅ Structured data (invoices, forms, receipts)
- ✅ Metadata extraction
- ✅ Multi-page documents
- ✅ Mixed content types

---

## 🚀 Quick Start

### 1. Install PDF Dependencies

```bash
pip install PyPDF2 pdfplumber tabula-py camelot-py[cv]
```

**System Requirements:**
- Java Runtime (for tabula-py)
- Ghostscript (for camelot-py)

**macOS:**
```bash
brew install ghostscript
brew install --cask java
```

**Ubuntu/Debian:**
```bash
sudo apt-get install ghostscript
sudo apt-get install default-jre
```

**Windows:**
- Download and install Java from java.com
- Download and install Ghostscript from ghostscript.com

---

## 📊 Supported PDF Types

### 1. **Tables in PDFs**

**Example:** Financial reports, data tables, spreadsheets

The pipeline automatically:
- Detects tables in PDF
- Extracts rows and columns
- Converts to structured records
- Preserves data types

**Extraction Modes:**
- `pdfplumber` - Primary method (works for most tables)
- `tabula-py` - Fallback method (Java-based)
- `camelot-py` - Advanced method (for complex tables)

### 2. **Text-Based PDFs**

**Example:** Reports, documents, articles

- Extracts all text content
- Preserves page structure
- Character and line counts
- Searchable content

### 3. **Forms and Invoices**

**Example:** Invoice PDFs, application forms, receipts

- Pattern-based extraction
- Automatic field detection
- Email, phone, date extraction
- Amount and total parsing

### 4. **Mixed Content**

**Example:** PDFs with both tables and text

- Combines multiple extraction methods
- Returns comprehensive data structure
- Preserves relationships

---

## 🎯 Usage Examples

### Upload PDF via Web Interface

1. Go to `http://localhost:5001`
2. Select a PDF file (tables, forms, or text)
3. Click "Process Data"
4. View extracted data and schema

### Upload PDF via API

```bash
# Upload PDF file
curl -X POST http://localhost:5001/api/v1/ingest \
  -F "file=@invoice.pdf" \
  -F "source_type=file"
```

### Programmatic Usage

```python
from pdf_extractor import PDFExtractor, PDFToDataConverter

# Create extractor
extractor = PDFExtractor()

# Extract tables
tables = extractor.extract_tables('data.pdf')
print(f"Found {len(tables)} tables")

# Extract all text
text_pages = extractor.extract_text('document.pdf')

# Extract structured data (invoices, forms)
patterns = {
    'invoice_number': r'Invoice\s*#?\s*:?\s*(\w+)',
    'total': r'Total\s*:?\s*\$?\s*([\d,]+\.?\d*)',
}
structured = extractor.extract_structured_data('invoice.pdf', patterns)

# Convert to records
converter = PDFToDataConverter()
records = converter.pdf_to_records('data.pdf', mode='auto')
```

---

## 🔧 Extraction Modes

### Mode: `auto` (Recommended)

Automatically tries all methods and returns best result:

```python
records = converter.pdf_to_records('data.pdf', mode='auto')
```

**Logic:**
1. Try table extraction first
2. If no tables, try structured patterns
3. If no patterns match, extract text

### Mode: `tables`

Extract only tables:

```python
records = converter.pdf_to_records('data.pdf', mode='tables')
```

**Best for:**
- Financial reports
- Data tables
- Spreadsheet-like PDFs

### Mode: `structured`

Use regex patterns to extract specific fields:

```python
records = converter.pdf_to_records('invoice.pdf', mode='structured')
```

**Best for:**
- Invoices
- Forms
- Receipts
- Applications

### Mode: `text`

Extract all text content:

```python
records = converter.pdf_to_records('document.pdf', mode='text')
```

**Best for:**
- Documents
- Articles
- Reports

---

## 📋 Example Use Cases

### Use Case 1: Extract Invoice Data

**Input:** `invoice_2024.pdf`

```
Invoice #12345
Date: 2024-01-15
Customer: John Doe
Email: john@example.com

Item          Qty   Price   Total
Laptop        1     $1200   $1200
Mouse         2     $25     $50
-----------------------------------
Subtotal:             $1250
Tax (10%):            $125
Total:                $1375
```

**Output:**

```json
[
  {
    "_pdf_type": "invoice",
    "metadata": {
      "invoice_number": ["12345"],
      "date": ["2024-01-15"],
      "email": ["john@example.com"],
      "total": ["1375"]
    },
    "line_items": [
      {
        "Item": "Laptop",
        "Qty": "1",
        "Price": "$1200",
        "Total": "$1200"
      },
      {
        "Item": "Mouse",
        "Qty": "2",
        "Price": "$25",
        "Total": "$50"
      }
    ]
  }
]
```

### Use Case 2: Extract Data Table

**Input:** `sales_report.pdf` with a table

**Output:**

```json
[
  {
    "Month": "January",
    "Sales": "50000",
    "Target": "45000",
    "Growth": "11%",
    "_pdf_page": 1,
    "_pdf_table": 0
  },
  {
    "Month": "February",
    "Sales": "52000",
    "Target": "47000",
    "Growth": "10.6%",
    "_pdf_page": 1,
    "_pdf_table": 0
  }
]
```

### Use Case 3: Extract Resume

**Input:** `resume.pdf`

```python
from pdf_extractor import PDFToDataConverter

converter = PDFToDataConverter()
records = converter.resume_pdf_to_records('resume.pdf')

# Output includes:
# - Full text
# - Extracted email, phone, LinkedIn, GitHub
# - Contact information
```

---

## 🎨 Data Schema Detection

The AI pipeline automatically detects schema from PDF data:

```python
# Example extracted data
[
  {
    "invoice_number": "12345",
    "date": "2024-01-15",
    "total": "1375.00",
    "email": "john@example.com"
  }
]

# AI-Detected Schema:
{
  "invoice_number": {
    "type": "string",
    "semantic_category": "identifier",
    "confidence": 0.95
  },
  "date": {
    "type": "date",
    "semantic_category": "temporal",
    "confidence": 1.0
  },
  "total": {
    "type": "float",
    "semantic_category": "monetary",
    "confidence": 1.0
  },
  "email": {
    "type": "email",
    "semantic_category": "contact",
    "confidence": 1.0
  }
}
```

---

## 💾 PDF Data Storage

All PDF-extracted data is stored in MongoDB with metadata:

```javascript
{
  "_id": ObjectId("..."),
  "invoice_number": "12345",
  "total": 1375.00,
  "email": "john@example.com",
  // PDF metadata
  "_pdf_page": 1,
  "_pdf_table": 0,
  "_pdf_source": "invoice_2024.pdf",
  // Pipeline metadata
  "_loaded_at": ISODate("2024-11-15T..."),
  "_data_quality_score": 95.5,
  "_is_anomaly": false
}
```

### Collections Used:

1. **`data`** - Extracted PDF records
2. **`schema_versions`** - PDF schema tracking
3. **`data_changes`** - Change detection
4. **`pdf_metadata`** - PDF file information (optional)

---

## 🔍 Advanced Features

### Custom Pattern Extraction

Define your own patterns for specific PDF types:

```python
from pdf_extractor import PDFExtractor

extractor = PDFExtractor()

# Custom patterns for medical records
medical_patterns = {
    'patient_id': r'Patient ID:\s*(\w+)',
    'doctor': r'Dr\.\s+([A-Z][a-z]+\s+[A-Z][a-z]+)',
    'diagnosis': r'Diagnosis:\s*(.+)',
    'medication': r'Medication:\s*(.+)',
}

data = extractor.extract_structured_data('medical_record.pdf', medical_patterns)
```

### Multi-Page Processing

Automatically handles multi-page PDFs:

```python
# Extract from 100-page PDF
records = converter.pdf_to_records('large_report.pdf', mode='auto')

# Each record includes page number
# {
#   "_pdf_page": 42,
#   "content": "..."
# }
```

### Batch PDF Processing

Process multiple PDFs at once:

```python
import os
from pdf_extractor import PDFToDataConverter

converter = PDFToDataConverter()
pdf_dir = '/path/to/pdfs'

all_records = []
for filename in os.listdir(pdf_dir):
    if filename.endswith('.pdf'):
        filepath = os.path.join(pdf_dir, filename)
        records = converter.pdf_to_records(filepath, mode='auto')

        # Add source file to each record
        for record in records:
            record['_source_file'] = filename

        all_records.extend(records)

print(f"Extracted {len(all_records)} records from {len(os.listdir(pdf_dir))} PDFs")
```

---

## 🚨 Troubleshooting

### Issue: "No tables found"

**Solution:**
- PDF might have images of tables (use OCR)
- Try different extraction methods
- Check if PDF is password-protected

### Issue: "Java not found" (tabula-py)

**Solution:**
```bash
# macOS
brew install java

# Ubuntu
sudo apt-get install default-jre

# Verify
java -version
```

### Issue: "Ghostscript not found" (camelot)

**Solution:**
```bash
# macOS
brew install ghostscript

# Ubuntu
sudo apt-get install ghostscript

# Verify
gs --version
```

### Issue: "Poor extraction quality"

**Solutions:**
1. PDF might be scanned image - use OCR
2. Try different mode: `mode='tables'` or `mode='structured'`
3. Use custom patterns for structured extraction
4. Consider pre-processing PDF (remove watermarks, etc.)

---

## 📊 Performance Tips

1. **Large PDFs** - Process in chunks
2. **Many PDFs** - Use batch processing with parallel workers
3. **Complex tables** - Use camelot-py for better accuracy
4. **Scanned PDFs** - Add OCR preprocessing (tesseract)

---

## 🎓 Best Practices

1. **Test extraction** - Always verify first page before processing full PDF
2. **Custom patterns** - Define patterns for consistent PDF structures
3. **Validation** - Check extracted data quality
4. **Metadata** - Store source PDF filename and page numbers
5. **Error handling** - Handle corrupted or encrypted PDFs gracefully

---

## 🔮 Future Enhancements

- [ ] OCR support for scanned PDFs
- [ ] PDF form field extraction
- [ ] Image extraction from PDFs
- [ ] Multi-language support
- [ ] PDF generation from data

---

## 📞 Support

If you encounter issues with PDF extraction:

1. Check logs: `logs/etl.log`
2. Verify dependencies: `pip list | grep -i pdf`
3. Test with sample PDFs first
4. Check Java and Ghostscript installation

---

**Happy PDF Processing! 📄✨**
