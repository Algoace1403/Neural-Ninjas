# 🤖 AI Schema Categorization Guide

## Overview
Your Dynamic ETL Pipeline now features **40+ semantic categories** for intelligent field classification! The AI automatically analyzes field names and values to categorize them into meaningful groups.

---

## 📊 All Categories

### 💰 Financial & Monetary (2 categories)

#### 1. **Monetary** 💰
- **Fields**: price, cost, amount, salary, fee, rate, charge, total, subtotal, tax, discount, revenue, budget, payment, invoice, bill
- **Examples**: `price`, `salary`, `total_cost`, `tax_amount`
- **Semantic Type**: `financial`

#### 2. **Financial Account** 🏦
- **Fields**: account, iban, swift, routing, bank, credit, debit
- **Examples**: `account_number`, `iban_code`, `bank_account`
- **Semantic Type**: `financial`

---

### 🔑 Identity & Authentication (3 categories)

#### 3. **Identifier** 🔑
- **Fields**: id, identifier, uuid, key, code, reference, number, serial, sku
- **Examples**: `user_id`, `product_sku`, `order_code`
- **Semantic Type**: `identity`

#### 4. **Authentication** 🔐
- **Fields**: password, token, secret, hash, salt, api_key, auth
- **Examples**: `password_hash`, `api_token`, `secret_key`
- **Semantic Type**: `security`

#### 5. **Session** 🎫
- **Fields**: session, cookie, jwt, bearer, oauth
- **Examples**: `session_id`, `jwt_token`, `oauth_token`
- **Semantic Type**: `security`

---

### 👤 Personal Information (3 categories)

#### 6. **Personal Name** 👤
- **Fields**: name, firstname, lastname, fullname, username, author, person, display_name
- **Examples**: `first_name`, `username`, `author_name`
- **Semantic Type**: `personal_info`

#### 7. **Age & Demographic** 🎂
- **Fields**: age, birthdate, dob, birthday, born
- **Examples**: `age`, `date_of_birth`, `birthday`
- **Semantic Type**: `personal_info`

#### 8. **Gender** ⚥
- **Fields**: gender, sex, pronoun
- **Examples**: `gender`, `sex`, `preferred_pronoun`
- **Semantic Type**: `personal_info`

---

### 📧 Contact Information (2 categories)

#### 9. **Contact** 📧
- **Fields**: email, phone, mobile, tel, contact, fax, cell
- **Examples**: `email_address`, `phone_number`, `mobile`
- **Semantic Type**: `contact_info`

#### 10. **Social Media** 📱
- **Fields**: twitter, facebook, linkedin, instagram, social, handle
- **Examples**: `twitter_handle`, `facebook_url`, `social_handle`
- **Semantic Type**: `contact_info`

---

### 📅 Temporal (2 categories)

#### 11. **Temporal** 📅
- **Fields**: date, time, timestamp, created, updated, modified, year, month, day, scheduled
- **Examples**: `created_at`, `updated_on`, `scheduled_date`
- **Semantic Type**: `temporal`

#### 12. **Duration** ⏱️
- **Fields**: duration, period, interval, elapsed, length, timeout
- **Examples**: `duration_minutes`, `timeout_seconds`, `elapsed_time`
- **Semantic Type**: `temporal`

---

### 🌍 Geographic & Location (2 categories)

#### 13. **Location** 📍
- **Fields**: address, city, state, country, zip, postal, location, region, province
- **Examples**: `address`, `city_name`, `postal_code`, `country`
- **Semantic Type**: `geographic`

#### 14. **Coordinates** 🌍
- **Fields**: latitude, longitude, lat, lng, lon, coord, geo
- **Examples**: `latitude`, `longitude`, `geo_coordinates`
- **Semantic Type**: `geographic`

---

### 📊 Measurement & Metrics (5 categories)

#### 15. **Rating** ⭐
- **Fields**: rating, score, rank, stars, review, feedback, grade
- **Examples**: `user_rating`, `review_score`, `star_rating`
- **Semantic Type**: `measurement`

#### 16. **Quantity** 📊
- **Fields**: quantity, count, number, total, amount, volume, size, stock, inventory
- **Examples**: `quantity`, `item_count`, `stock_level`
- **Semantic Type**: `measurement`

#### 17. **Percentage** 📈
- **Fields**: percentage, percent, ratio, rate, proportion
- **Examples**: `discount_percentage`, `completion_rate`, `ratio`
- **Semantic Type**: `measurement`

#### 18. **Weight & Mass** ⚖️
- **Fields**: weight, mass, kg, lb, gram, ounce
- **Examples**: `weight_kg`, `mass_grams`, `weight_lbs`
- **Semantic Type**: `measurement`

#### 19. **Temperature** 🌡️
- **Fields**: temperature, temp, celsius, fahrenheit, kelvin
- **Examples**: `temp_celsius`, `temperature_f`, `temp`
- **Semantic Type**: `measurement`

---

### 📝 Text & Content (3 categories)

#### 20. **Description** 📝
- **Fields**: description, details, info, summary, text, content, notes, bio, about
- **Examples**: `description`, `product_details`, `bio`, `notes`
- **Semantic Type**: `textual`

#### 21. **Title & Heading** 📰
- **Fields**: title, heading, headline, subject, topic
- **Examples**: `title`, `headline`, `subject_line`
- **Semantic Type**: `textual`

#### 22. **Comment & Message** 💬
- **Fields**: comment, message, post, reply, chat, note
- **Examples**: `user_comment`, `message_text`, `chat_message`
- **Semantic Type**: `textual`

---

### 🎬 Media & Files (4 categories)

#### 23. **URL** 🔗
- **Fields**: url, link, website, uri, href, endpoint
- **Examples**: `website_url`, `product_link`, `api_endpoint`
- **Semantic Type**: `reference`

#### 24. **File Path** 📁
- **Fields**: file, path, filename, directory, folder, attachment
- **Examples**: `file_path`, `document_name`, `attachment`
- **Semantic Type**: `reference`

#### 25. **Image & Media** 🖼️
- **Fields**: image, photo, picture, avatar, thumbnail, icon, logo
- **Examples**: `profile_image`, `product_photo`, `avatar_url`
- **Semantic Type**: `media`

#### 26. **Video & Audio** 🎬
- **Fields**: video, audio, media, mp4, mp3, stream
- **Examples**: `video_url`, `audio_file`, `stream_link`
- **Semantic Type**: `media`

---

### 🚦 Status & State (2 categories)

#### 27. **Status** 🚦
- **Fields**: status, state, condition, flag, active, enabled, live, published
- **Examples**: `order_status`, `is_active`, `published_state`
- **Semantic Type**: `categorical`

#### 28. **Priority** ⚡
- **Fields**: priority, importance, urgency, severity, level
- **Examples**: `priority_level`, `urgency`, `severity`
- **Semantic Type**: `categorical`

---

### 🏷️ Classification (2 categories)

#### 29. **Category** 🏷️
- **Fields**: category, type, kind, class, group, tag, genre, department
- **Examples**: `product_category`, `item_type`, `department`
- **Semantic Type**: `categorical`

#### 30. **Tag & Label** #️⃣
- **Fields**: tag, label, badge, keyword, hashtag
- **Examples**: `tags`, `labels`, `keywords`
- **Semantic Type**: `categorical`

---

### 🏥 Health & Medical (2 categories)

#### 31. **Medical** 🏥
- **Fields**: diagnosis, symptom, disease, condition, medication, prescription, patient
- **Examples**: `diagnosis`, `symptoms`, `patient_id`, `medication`
- **Semantic Type**: `medical`

#### 32. **Health Metric** ❤️
- **Fields**: blood_pressure, heart_rate, glucose, bmi, pulse
- **Examples**: `blood_pressure`, `heart_rate_bpm`, `glucose_level`
- **Semantic Type**: `medical`

---

### 🎓 Education (1 category)

#### 33. **Academic** 🎓
- **Fields**: grade, course, subject, degree, major, gpa, student, teacher
- **Examples**: `student_grade`, `course_name`, `gpa`, `degree`
- **Semantic Type**: `education`

---

### 📦 Business & Commerce (2 categories)

#### 34. **Product** 📦
- **Fields**: product, item, goods, merchandise, sku, model
- **Examples**: `product_name`, `item_sku`, `model_number`
- **Semantic Type**: `commerce`

#### 35. **Company** 🏢
- **Fields**: company, organization, business, enterprise, firm, corporation
- **Examples**: `company_name`, `organization`, `business_name`
- **Semantic Type**: `business`

---

### 🌐 Technical & System (3 categories)

#### 36. **IP & Network** 🌐
- **Fields**: ip, ipaddress, hostname, domain, server, port
- **Examples**: `ip_address`, `hostname`, `server_name`, `port`
- **Semantic Type**: `technical`

#### 37. **Version** 🔢
- **Fields**: version, release, build, revision
- **Examples**: `version`, `release_number`, `build_id`
- **Semantic Type**: `technical`

#### 38. **Error & Log** ⚠️
- **Fields**: error, exception, warning, log, debug, trace
- **Examples**: `error_message`, `exception_type`, `log_level`
- **Semantic Type**: `technical`

---

## 🎯 How It Works

### 1. **Field Name Analysis**
The AI analyzes field names using:
- **Keyword matching**: Looks for specific keywords in field names
- **Pattern matching**: Uses regex patterns to detect formats
- **Confidence scoring**: Assigns confidence scores (0-1) to each match

### 2. **Value Analysis** (when applicable)
- Analyzes sample values to verify categorization
- Checks data types, formats, and patterns
- Calculates uniqueness ratios and cardinality

### 3. **Icon Assignment**
Each category gets a unique emoji icon for easy visual identification!

---

## 📊 Enhanced Schema Display

Your schema now shows:

| Column | Description |
|--------|-------------|
| **Icon** | Visual emoji representing the category |
| **Field Name** | The actual field name |
| **Data Type** | Python/JSON type (string, number, boolean, etc.) |
| **Category** | Specific subcategory (e.g., "Monetary", "Contact") |
| **Semantic Type** | Broader category group (e.g., "financial", "personal_info") |
| **Sample Values** | Example values from your data |

---

## 🎨 Category Distribution Dashboard

After processing, you'll see a **Category Distribution** section showing:
- Count of fields in each semantic type
- Visual cards with category names and counts
- Color-coded display for easy identification

---

## 🧪 Test It Out!

### Sample File Created
I've created a comprehensive test file: `/tmp/sample_all_categories.json`

This file includes examples of **ALL 38 categories**:
- Financial data (price, salary, account_number)
- Personal info (name, age, gender, birthdate)
- Contact info (email, phone, social media)
- Location data (address, city, coordinates)
- Measurements (ratings, quantities, percentages, weight, temperature)
- Media (URLs, images, videos, files)
- Business data (products, companies, departments)
- Health metrics (blood_pressure, heart_rate, diagnosis)
- Technical data (IP addresses, versions, error logs)
- And much more!

### How to Test
1. Go to **http://localhost:5001**
2. Upload `/tmp/sample_all_categories.json`
3. Select "Auto-Detect" for both Source and Entity
4. Click "Upload & Process"
5. See the **AI-Inferred Schema** with 40+ fields categorized!

---

## 💡 Benefits

### For Data Engineers
- **Quick data understanding**: Instantly see what types of data you're dealing with
- **Data governance**: Identify sensitive fields (authentication, personal info, medical)
- **Schema evolution tracking**: See how schemas change over time

### For Business Users
- **Visual clarity**: Icons and colors make data easy to understand
- **Category insights**: See distribution of data types at a glance
- **Quality assurance**: Verify data is categorized correctly

### For Compliance & Security
- **PII detection**: Automatically identifies personal information
- **Sensitive data flagging**: Highlights authentication, medical, financial data
- **GDPR/HIPAA compliance**: Helps track sensitive data categories

---

## 🔧 Customization

Want to add your own categories? Edit `ai_schema_inference.py`:

```python
FIELD_CATEGORIES = {
    'your_custom_category': {
        'keywords': ['keyword1', 'keyword2'],
        'patterns': [r'pattern1', r'pattern2'],
        'semantic_type': 'your_semantic_type',
        'icon': '🎯'
    }
}
```

---

## 📈 What's Next?

Future enhancements could include:
- ML-based category learning from data patterns
- Custom category definitions per domain
- Automatic data quality scoring per category
- Relationship detection between categories
- Privacy compliance auto-reporting

---

## ✅ Summary

Your AI-Inferred Schema now provides:
- ✅ **40+ categories** covering all common data types
- ✅ **Visual icons** for quick identification
- ✅ **Semantic types** for grouping related categories
- ✅ **Category distribution** dashboard
- ✅ **Automatic detection** from field names and values
- ✅ **Confidence scores** for each classification

**Try it now at http://localhost:5001!** 🚀
