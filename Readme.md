# 📊 E-Commerce Traffic Analytics Dashboard

**Designer:** i_courner/god ✨  
**Version:** 1.0.0  
**Status:** ✅ Production Ready  
**Data:** India E-Commerce Website Traffic (Jan–Nov 2024)

---

## 🎯 Project Overview

A professional, interactive **Streamlit-based analytics dashboard** that visualizes e-commerce website traffic data for India. Features cutting-edge **3D visualizations**, real-time filtering, and business intelligence insights across 15,004 user sessions and 22 data columns.

---

## ⚡ Quick Start (3 Steps)

### Step 1 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2 — Run the App
```bash
streamlit run app.py
```

### Step 3 — Open Browser
```
http://localhost:8501
```

> ✅ That's it! Your dashboard is running.

---

## 📁 Project Files

```
ecommerce-dashboard/
│
├── app.py                                  ← Main Streamlit application (1000+ lines)
├── requirements.txt                        ← Python dependencies
├── README.md                               ← This file
└── Ecommerce_Website_Traffic_India.xlsx    ← Dataset (15,004 records)
```

> ⚠️ **Important:** The Excel file must be named exactly `Ecommerce_Website_Traffic_India.xlsx` and placed in the **same folder** as `app.py`.

---

## 🎨 Dashboard Features

### 📈 KPI Metrics (Top Section)
| Metric | Description |
|--------|-------------|
| Total Sessions | Count of active user sessions |
| Conversion Rate | Purchase conversion percentage |
| Avg Order Value | Average revenue per order (₹) |
| Bounce Rate | Session abandonment rate |

---

### 🔷 4 Interactive 3D Visualization Tabs

#### Tab 1 — 3D Scatter Analysis
- X-axis: Session Duration (seconds)
- Y-axis: Pages Viewed per session
- Z-axis: Order Value (₹)
- Color-coded by revenue intensity
- Rotate and zoom interactively

#### Tab 2 — Geographic 3D Analysis
- Top 15 Indian states plotted in 3D
- X: Total Sessions | Y: Total Purchases | Z: Total Revenue
- Bubble size represents revenue volume

#### Tab 3 — Time Series 3D
- Daily traffic trends over Jan–Nov 2024
- Identifies seasonal and festival-driven spikes
- 3D surface/line view for temporal patterns

#### Tab 4 — Product Category 3D
Five product categories analyzed:
- 🏠 Home Appliances
- 🖥️ Office Equipment
- 💄 Beauty Products
- 👗 Clothing
- 📱 Technical Devices

---

### 📊 Detailed Analytics Section

1. **Traffic Source Performance** — Revenue by Organic / Paid / Direct / Social / Referral
2. **Device Type Conversion** — Conversion rates for Mobile / Desktop / Tablet
3. **Age Group Distribution** — Pie chart of sessions by age group (10–50 years)
4. **Festival Impact Analysis** — Revenue comparison across Diwali, Holi, Navratri, Pongal

### 🔥 Additional Features
- **Correlation Heatmap** — Relationships between 8 numeric variables
- **Expandable Raw Data Table** — First 100 records with key columns
- **Real-time Filters** — All charts update instantly on filter change

---

## 🔍 Sidebar Filters

| Filter | Options |
|--------|---------|
| 📅 Date Range | Jan 2024 – Nov 2024 |
| 🔗 Traffic Source | Organic, Paid, Direct, Social, Referral |
| 📱 Device Type | Mobile, Desktop, Tablet |
| 🎉 Festival | Diwali, Holi, Navratri, Pongal, None |

---

## 📊 Dataset Overview

| Property | Value |
|----------|-------|
| File | `Ecommerce_Website_Traffic_India.xlsx` |
| Records | 15,004 sessions |
| Columns | 22 attributes |
| Date Range | January – November 2024 |
| Geography | All Indian states |

### Key Columns Explained

| Column | Description |
|--------|-------------|
| `date` | Session date |
| `user_id` | Unique user identifier |
| `time` | Session timestamp |
| `traffic_source` | How user arrived (Organic/Paid/etc.) |
| `device` | Device type (Mobile/Desktop/Tablet) |
| `city` | User's city |
| `state` | User's state |
| `age` | User age (10–50) |
| `gender` | User gender |
| `session_duration_sec` | Time spent on site (20–4,500 sec) |
| `pages_viewed` | Pages browsed per session (1–25) |
| `bounce` | Whether user bounced (0/1) |
| `product_viewed` | Product category viewed |
| `add_to_cart` | Whether item was added to cart (0/1) |
| `purchase` | Whether purchase was made (0/1) |
| `order_value` | Order amount in ₹ (0–39,962) |
| `festival` | Festival context of session |
| `category` | Product category |

### Data Quality
- 15,003 complete records (99.99%)
- 1 missing `user_id` handled automatically
- 1 missing `time` value handled automatically
- No duplicate records
- Missing numeric values filled with column mean

---

## 🎨 Color Scheme

| Color | Hex | Usage |
|-------|-----|-------|
| 🟦 Dark Blue | `#0F3460` | Headers, primary text |
| 🟦 Navy | `#16213E` | Sidebar background |
| 🔴 Coral Red | `#E94560` | Highlights, buttons, accents |
| 🔵 Cyan | `#00D4FF` | Positive metrics |
| 🟡 Gold | `#FFB703` | Secondary metrics |
| 🟥 Light Red | `#FF6B6B` | Bounce rate, warnings |
| ⬜ Light Gray | `#F8F9FA` | Page background |

---

## 🛠️ Technical Stack

| Component | Technology |
|-----------|-----------|
| Web Framework | Streamlit |
| Data Processing | Pandas, NumPy |
| Visualizations | Plotly (3D + 2D) |
| Data Source | Excel (.xlsx) via OpenPyXL |
| Language | Python 3.8+ |

---

## 🔧 Customization Guide

### Change Dashboard Title
Edit line 12 in `app.py`:
```python
page_title="Your Custom Title",
```

### Change Primary Color
Edit CSS in `app.py` (around line 25):
```python
--primary: #YOUR_HEX_CODE;
--accent: #YOUR_HEX_CODE;
```

### Add a New Filter
In the sidebar section of `app.py`:
```python
new_filter = st.sidebar.multiselect(
    "🏷️ Your Label",
    options=df['your_column'].unique(),
    default=df['your_column'].unique()
)
filtered_df = filtered_df[filtered_df['your_column'].isin(new_filter)]
```

---

## 🚀 Deployment

### Local (Development)
```bash
streamlit run app.py
# Visit: http://localhost:8501
```

### Streamlit Cloud (Recommended — Free)
1. Push all files to a GitHub repository
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your GitHub repo
4. Set `app.py` as the main module
5. Click **Deploy** — you'll get a public shareable link

> 📌 Make sure `Ecommerce_Website_Traffic_India.xlsx` is committed to the repo root.

### Different Port (if 8501 is busy)
```bash
streamlit run app.py --server.port 8502
```

---

## 🆘 Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| `ModuleNotFoundError` | Packages not installed | `pip install -r requirements.txt` |
| `FileNotFoundError` on xlsx | Wrong filename or location | Ensure `Ecommerce_Website_Traffic_India.xlsx` is in same folder as `app.py` |
| Port 8501 in use | Another app running | Use `--server.port 8502` |
| Charts load slowly | Large unfiltered dataset | Apply sidebar filters to reduce data |
| Colors look wrong | Browser cache | Press `Ctrl+F5` to hard refresh |
| Streamlit Cloud install fails | Bad package version in requirements | Use `>=` version constraints, not `==` |

### Verify Installation
```bash
python -c "import streamlit; print('Streamlit:', streamlit.__version__)"
python -c "import plotly; print('Plotly:', plotly.__version__)"
python -c "import pandas; print('Pandas:', pandas.__version__)"
python -c "import openpyxl; print('OpenPyXL:', openpyxl.__version__)"
```

### Clear Cache
```bash
streamlit cache clear
```

---

## 💡 Key Business Insights to Explore

1. **Which traffic source drives the most revenue?**
   → Use the Traffic Source Performance chart

2. **What's the mobile vs desktop conversion difference?**
   → Use the Device Type Conversion chart

3. **Which age group spends the most?**
   → Use the Age Group Distribution pie chart

4. **How does Diwali impact sales vs other festivals?**
   → Apply the Festival filter and compare KPI metrics

5. **Which state is the best market?**
   → Use the Geographic 3D tab

6. **Is there a correlation between pages viewed and purchase?**
   → Use the Correlation Heatmap

---

## 📱 Browser Compatibility

| Browser | Support |
|---------|---------|
| Chrome / Chromium | ✅ Recommended |
| Firefox | ✅ Full support |
| Microsoft Edge | ✅ Full support |
| Safari | ✅ Works well |
| Mobile browsers | ✅ Responsive design |
| Internet Explorer | ❌ Not supported |

---

## 🔐 Data Privacy

- ✅ All data processing is done **locally** on your machine
- ✅ No data is sent to external servers
- ✅ No analytics or tracking embedded
- ✅ Safe for confidential business data

---

## 📚 Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plotly 3D Charts](https://plotly.com/python/3d-charts/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Python Getting Started](https://www.python.org/about/getting-started/)

---

## 🔄 System Requirements

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| Python | 3.8+ | 3.10+ |
| RAM | 4 GB | 8 GB |
| Disk Space | 500 MB | 1 GB |
| CPU | 2 GHz | 4+ GHz |
| Browser | Chrome/Firefox | Chrome (latest) |

---

## 👤 Credits

**Dashboard Designer:** i_courner/god ✨  
**Version:** 1.0.0  
**Dataset:** India E-Commerce Website Traffic (Jan–Nov 2024)  
**Status:** ✅ Production Ready

---

**Happy analyzing! 📊📈**
