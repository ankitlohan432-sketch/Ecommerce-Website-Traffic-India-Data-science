# 📊 E-Commerce Traffic Analytics Dashboard — India

> A professional, fully 3D dark-themed analytics dashboard built with **Python + Streamlit + Plotly**.  
> Designed by **Ankit** · Dataset: India E-Commerce Website Traffic

---

## 🖥️ Live Preview

![Dashboard Preview](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3D%20Charts-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

---

## ✨ Features

### 📈 KPI Cards
- **Total Sessions** — Live count of filtered user sessions
- **Conversion Rate** — Purchase-to-session percentage
- **Average Order Value** — Mean revenue per order in ₹
- **Bounce Rate** — Percentage of sessions with no action

### 🎨 Advanced 3D Analytics (4 Tabs)
| Tab | Chart | Description |
|-----|-------|-------------|
| 📊 3D Scatter | `Scatter3d` | Session Duration × Pages Viewed × Order Value |
| 🗺️ Geographic 3D | `Scatter3d` | Top 15 States — Sessions × Purchases × Revenue |
| ⏰ Time Series 3D | `Scatter3d + Lines` | Daily Traffic & Revenue Trend over time |
| 🛍️ Product Category 3D | `Scatter3d` | 5 product categories — Views × Purchases × Revenue |

### 📊 Detailed Performance Metrics (All 3D)
- **Revenue by Traffic Source** — 3D Mesh bar chart (6 sources)
- **Conversion Rate by Device** — 3D Mesh bar chart (Mobile / Desktop / Tablet)
- **Age Group Analysis** — 3D Bubble Scatter (sessions, revenue, conversion)
- **Festival Revenue Impact** — 3D Mesh bar chart (Diwali, Holi, etc.)

### 🔥 Correlation Surface
- **3D Surface Plot** of the full 8-feature correlation matrix using `go.Surface` with contour projections

### 📋 Raw Data Table
- Filterable preview of up to 100 records with all key columns

---

## 🗂️ Project Structure

```
📦 ecommerce-dashboard/
├── app.py                              # Main Streamlit application
├── requirements.txt                    # Python dependencies
├── Ecommerce_Website_Traffic_India.xlsx  # Dataset (place in same folder)
└── README.md                           # This file
```

---

## ⚙️ Installation & Setup

### 1. Clone or download the project

```bash
git clone https://github.com/your-username/ecommerce-dashboard.git
cd ecommerce-dashboard
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Place your dataset

Make sure `Ecommerce_Website_Traffic_India.xlsx` is in the **same folder** as `app.py`.

### 5. Run the dashboard

```bash
streamlit run app.py
```

The app will open automatically at **http://localhost:8501**

---

## 🌐 Deploy on Streamlit Cloud (Free)

1. Push your project to a **GitHub repository**
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **"New app"** → connect your GitHub repo
4. Set **Main file path** to `app.py`
5. Click **Deploy** ✅

> ⚠️ Make sure `Ecommerce_Website_Traffic_India.xlsx` is committed to your repo alongside `app.py`.

---

## 🔧 Sidebar Filters

| Filter | Type | Description |
|--------|------|-------------|
| 📅 Date Range | Date picker | Filter all charts by date window |
| 🔗 Traffic Source | Multi-select | Direct, Organic Search, Paid Ads, Social Media, Email, Referral |
| 📱 Device Type | Multi-select | Mobile, Desktop, Tablet |
| 🎉 Festival | Multi-select | Diwali, Holi, No Festival, etc. |

All filters apply **globally** across every chart and KPI.

---

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `streamlit` | ≥ 1.28.0 | Web app framework |
| `pandas` | ≥ 2.2.0 | Data loading & manipulation |
| `numpy` | ≥ 1.26.0 | Numerical operations |
| `plotly` | ≥ 5.18.0 | All 2D and 3D interactive charts |
| `openpyxl` | ≥ 3.1.0 | Reading `.xlsx` Excel files |
| `python-dateutil` | ≥ 2.8.2 | Robust date parsing |
| `pytz` | ≥ 2023.3 | Timezone handling |

---

## 📁 Dataset Columns

| Column | Type | Description |
|--------|------|-------------|
| `date` | date | Session date |
| `time` | string | Session time |
| `user_id` | string | Unique user identifier |
| `traffic_source` | string | How the user arrived |
| `device` | string | Mobile / Desktop / Tablet |
| `city` | string | User's city |
| `state` | string | User's state (India) |
| `session_duration_sec` | int | Length of session in seconds |
| `pages_viewed` | int | Number of pages visited |
| `bounce` | int (0/1) | Whether session bounced |
| `product_viewed` | int | Products viewed count |
| `home_appliances` | int (0/1) | Category flag |
| `office_equipments` | int (0/1) | Category flag |
| `beauty_products` | int (0/1) | Category flag |
| `clothing` | int (0/1) | Category flag |
| `technical_devices` | int (0/1) | Category flag |
| `add_to_cart` | int | Items added to cart |
| `purchase` | int (0/1) | Whether purchase was made |
| `order_value` | float | Revenue in ₹ |
| `age` | int | User age |
| `gender` | string | User gender |
| `festival` | string | Active festival during session |

---

## 🎨 Design System

| Element | Value |
|---------|-------|
| Background | `#080d1a` (deep navy) |
| Card background | `#111827` → `#1a2540` gradient |
| Accent blue | `#63b3ed` / `#90cdf4` |
| Accent coral | `#f6875f` |
| Accent gold | `#fbd38d` |
| Accent rose | `#fc8181` |
| Display font | Syne (Google Fonts) |
| Body font | DM Sans (Google Fonts) |

---

## 🛠️ Troubleshooting

**App crashes on startup?**
- Make sure the Excel file name is exactly `Ecommerce_Website_Traffic_India.xlsx` and is in the same folder as `app.py`

**Charts not showing?**
- Upgrade Plotly: `pip install --upgrade plotly`

**Filters show no data?**
- Try resetting filters — all multiselects must have at least one option selected

**Fonts not loading?**
- The app loads Google Fonts from the internet. If you're offline, it will fall back to system fonts gracefully.

---

## 👨‍💻 Author

**Ankit**  
👨‍💻  Data Scientist & Ai Developer  

---

## 📄 License

This project is for educational and portfolio purposes.  
Feel free to fork, modify, and deploy with credit.
