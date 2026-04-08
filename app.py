import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# Page Configuration
st.set_page_config(
    page_title="E-commerce Traffic Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM CSS STYLING
# ============================================================================
st.markdown("""
<style>
    /* Primary Color Scheme */
    :root {
        --primary: #0F3460;
        --secondary: #16213E;
        --accent: #E94560;
        --success: #00D4FF;
        --warning: #FFB703;
        --bg-light: #F8F9FA;
        --text-dark: #1A1A1A;
    }
    
    /* Main Container */
    .main {
        background-color: #F8F9FA;
    }
    
    /* Header Styling */
    .header-container {
        background: linear-gradient(135deg, #0F3460 0%, #16213E 100%);
        padding: 40px;
        border-radius: 15px;
        margin-bottom: 30px;
        color: white;
        box-shadow: 0 8px 32px rgba(15, 52, 96, 0.2);
    }
    
    .header-container h1 {
        font-size: 3em;
        font-weight: 700;
        margin: 0;
        letter-spacing: -1px;
    }
    
    .header-container p {
        font-size: 1.1em;
        margin: 10px 0 0 0;
        opacity: 0.9;
    }
    
    /* Designer Credit */
    .designer-credit {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: linear-gradient(135deg, #E94560 0%, #FF6B6B 100%);
        color: white;
        padding: 12px 20px;
        border-radius: 30px;
        font-weight: 600;
        font-size: 0.9em;
        box-shadow: 0 4px 15px rgba(233, 69, 96, 0.3);
        z-index: 100;
        letter-spacing: 0.5px;
    }
    
    /* Metric Cards */
    .metric-card {
        background: white;
        padding: 25px;
        border-radius: 12px;
        border-left: 5px solid #E94560;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
    }
    
    /* Section Divider */
    .section-divider {
        border-bottom: 2px solid #E94560;
        margin: 30px 0;
        padding-bottom: 10px;
    }
    
    /* Filter Panels */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #16213E 0%, #0F3460 100%);
    }
    
    [data-testid="stSidebar"] label {
        color: #00D4FF !important;
        font-weight: 600;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #E94560 0%, #FF6B6B 100%);
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        padding: 12px 30px;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(233, 69, 96, 0.4);
    }
    
    /* Text Styling */
    h2, h3 {
        color: #0F3460;
        font-weight: 700;
        margin-top: 30px;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        border-bottom: 2px solid #E94560;
    }
    
    .stTabs [aria-selected="true"] {
        color: #E94560 !important;
        font-weight: 700;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: #F0F4F8;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# LOAD AND PREPARE DATA
# ============================================================================
@st.cache_data
def load_data():
    df = pd.read_excel('Ecommerce_Website_Traffic_India.xlsx')
    
    # Data Cleaning
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    df = df.drop_duplicates()
    df = df.dropna(subset=['user_id', 'time'])
    
    # Convert date column
    df['date'] = pd.to_datetime(df['date'])
    
    # Fill missing numeric values
    numeric_cols = df.select_dtypes(include=np.number).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    
    return df

df = load_data()

# ============================================================================
# SIDEBAR FILTERS
# ============================================================================
st.sidebar.markdown("### 🎯 FILTERS")
st.sidebar.markdown("---")

# Date Range Filter
date_range = st.sidebar.date_input(
    "📅 Select Date Range",
    value=(df['date'].min(), df['date'].max()),
    min_value=df['date'].min(),
    max_value=df['date'].max()
)

# Traffic Source Filter
traffic_sources = st.sidebar.multiselect(
    "🔗 Traffic Source",
    options=df['traffic_source'].unique(),
    default=df['traffic_source'].unique()
)

# Device Filter
devices = st.sidebar.multiselect(
    "📱 Device Type",
    options=df['device'].unique(),
    default=df['device'].unique()
)

# Festival Filter
festivals = st.sidebar.multiselect(
    "🎉 Festival",
    options=df['festival'].unique(),
    default=df['festival'].unique()
)

# Apply Filters
filtered_df = df[
    (df['date'].dt.date >= date_range[0]) &
    (df['date'].dt.date <= date_range[1]) &
    (df['traffic_source'].isin(traffic_sources)) &
    (df['device'].isin(devices)) &
    (df['festival'].isin(festivals))
].copy()

# ============================================================================
# HEADER
# ============================================================================
st.markdown("""
<div class="header-container">
    <h1>📊 E-Commerce Traffic Analytics</h1>
    <p>Advanced insights into India's e-commerce website traffic patterns & user behavior</p>
</div>
""", unsafe_allow_html=True)

# Designer Credit
st.markdown("""
<div class="designer-credit">
    🎨 Designer: i_courner/god
</div>
""", unsafe_allow_html=True)

# ============================================================================
# KEY METRICS (3D-STYLE CARDS)
# ============================================================================
st.markdown("### 📈 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <h4>👥 Total Sessions</h4>
        <h2 style="color: #E94560; font-size: 2.5em; margin: 10px 0;">{len(filtered_df):,}</h2>
        <p style="color: #999; margin: 0;">Active User Sessions</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    conversion_rate = (filtered_df['purchase'].sum() / len(filtered_df)) * 100
    st.markdown(f"""
    <div class="metric-card">
        <h4>🎯 Conversion Rate</h4>
        <h2 style="color: #00D4FF; font-size: 2.5em; margin: 10px 0;">{conversion_rate:.2f}%</h2>
        <p style="color: #999; margin: 0;">Purchase Conversion</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    avg_order_value = filtered_df['order_value'].mean()
    st.markdown(f"""
    <div class="metric-card">
        <h4>💰 Avg Order Value</h4>
        <h2 style="color: #FFB703; font-size: 2.5em; margin: 10px 0;">₹{avg_order_value:,.0f}</h2>
        <p style="color: #999; margin: 0;">Average Revenue</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    bounce_rate = (filtered_df['bounce'].sum() / len(filtered_df)) * 100
    st.markdown(f"""
    <div class="metric-card">
        <h4>📉 Bounce Rate</h4>
        <h2 style="color: #FF6B6B; font-size: 2.5em; margin: 10px 0;">{bounce_rate:.2f}%</h2>
        <p style="color: #999; margin: 0;">Session Exits</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# ============================================================================
# 3D VISUALIZATIONS - MAIN SECTION
# ============================================================================
st.markdown("### 🎨 Advanced 3D Analytics")

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 3D Scatter Analysis",
    "🗺️ Geographic 3D",
    "⏰ Time Series 3D",
    "🛍️ Product Category 3D"
])

# ============================================================================
# TAB 1: 3D SCATTER - Session Duration vs Pages vs Order Value
# ============================================================================
with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("#### Session Metrics 3D Analysis")
        
        fig_3d_scatter = go.Figure(data=[go.Scatter3d(
            x=filtered_df['session_duration_sec'],
            y=filtered_df['pages_viewed'],
            z=filtered_df['order_value'],
            mode='markers',
            marker=dict(
                size=filtered_df['order_value'].apply(lambda x: max(3, min(15, x/200))),
                color=filtered_df['order_value'],
                colorscale='Viridis',
                colorbar=dict(
                    title="Order Value (₹)",
                    thickness=15,
                    len=0.7
                ),
                opacity=0.8,
                line=dict(width=0.5, color='white')
            ),
            text=[f"Duration: {d}s<br>Pages: {p}<br>Value: ₹{v:.0f}<br>Device: {dv}" 
                  for d, p, v, dv in zip(
                      filtered_df['session_duration_sec'],
                      filtered_df['pages_viewed'],
                      filtered_df['order_value'],
                      filtered_df['device']
                  )],
            hovertemplate='<b>Session Details</b><br>%{text}<extra></extra>',
            customdata=filtered_df['device']
        )])
        
        fig_3d_scatter.update_layout(
            title='<b>Session Duration vs Pages Viewed vs Order Value</b>',
            scene=dict(
                xaxis=dict(title='<b>Session Duration (seconds)</b>', backgroundcolor="#f0f0f0"),
                yaxis=dict(title='<b>Pages Viewed</b>', backgroundcolor="#f0f0f0"),
                zaxis=dict(title='<b>Order Value (₹)</b>', backgroundcolor="#f0f0f0"),
                camera=dict(
                    eye=dict(x=1.5, y=1.5, z=1.3)
                )
            ),
            height=600,
            margin=dict(l=0, r=0, b=0, t=50),
            template='plotly_white',
            font=dict(family="Arial, sans-serif", size=12, color="#0F3460")
        )
        
        st.plotly_chart(fig_3d_scatter, use_container_width=True)
    
    with col2:
        st.markdown("#### Insights")
        st.info("""
        **Key Findings:**
        
        - 🎯 Sessions with higher page views tend to have higher order values
        - ⏱️ Session duration positively correlates with purchases
        - 💡 Optimize user journey to increase pages viewed
        - 🔍 Focus on reducing bounce for high-value products
        """)

# ============================================================================
# TAB 2: GEOGRAPHIC 3D - State, City, Order Value
# ============================================================================
with tab2:
    st.markdown("#### Geographic Distribution - 3D View")
    
    # Aggregate by state
    state_data = filtered_df.groupby('state').agg({
        'order_value': 'sum',
        'user_id': 'count',
        'purchase': 'sum'
    }).reset_index()
    
    state_data.columns = ['state', 'total_value', 'sessions', 'purchases']
    state_data = state_data.sort_values('total_value', ascending=False).head(15)
    
    fig_3d_geo = go.Figure(data=[go.Scatter3d(
        x=state_data['sessions'],
        y=state_data['purchases'],
        z=state_data['total_value'],
        mode='markers+text',
        text=state_data['state'],
        textposition="top center",
        marker=dict(
            size=state_data['total_value'].apply(lambda x: max(5, min(20, x/1000))),
            color=state_data['total_value'],
            colorscale='Plasma',
            colorbar=dict(
                title="Revenue (₹)",
                thickness=15,
                len=0.7
            ),
            opacity=0.85,
            line=dict(width=1, color='white')
        ),
        hovertemplate='<b>%{text}</b><br>Sessions: %{x}<br>Purchases: %{y}<br>Revenue: ₹%{z:,.0f}<extra></extra>'
    )])
    
    fig_3d_geo.update_layout(
        title='<b>Top States: 3D Revenue Analysis</b>',
        scene=dict(
            xaxis=dict(title='<b>Total Sessions</b>'),
            yaxis=dict(title='<b>Total Purchases</b>'),
            zaxis=dict(title='<b>Total Revenue (₹)</b>'),
            camera=dict(eye=dict(x=1.5, y=1.5, z=1.3))
        ),
        height=700,
        template='plotly_white',
        font=dict(family="Arial, sans-serif", size=11, color="#0F3460")
    )
    
    st.plotly_chart(fig_3d_geo, use_container_width=True)

# ============================================================================
# TAB 3: TIME SERIES 3D
# ============================================================================
with tab3:
    st.markdown("#### Temporal Analysis - 3D View")
    
    # Create daily aggregates
    daily_data = filtered_df.groupby(filtered_df['date'].dt.date).agg({
        'user_id': 'count',
        'order_value': 'sum',
        'purchase': 'sum'
    }).reset_index()
    
    daily_data.columns = ['date', 'sessions', 'revenue', 'purchases']
    daily_data['date_num'] = range(len(daily_data))
    
    fig_3d_time = go.Figure(data=[go.Scatter3d(
        x=daily_data['date_num'],
        y=daily_data['sessions'],
        z=daily_data['revenue'],
        mode='markers+lines',
        marker=dict(
            size=daily_data['purchases'].apply(lambda x: max(4, min(12, x/2))),
            color=daily_data['revenue'],
            colorscale='Turbo',
            colorbar=dict(title="Revenue (₹)"),
            opacity=0.8
        ),
        line=dict(color='#0F3460', width=2),
        text=[f"Date: {d}<br>Sessions: {s}<br>Revenue: ₹{r:,.0f}<br>Purchases: {p}" 
              for d, s, r, p in zip(daily_data['date'], daily_data['sessions'], 
                                    daily_data['revenue'], daily_data['purchases'])],
        hovertemplate='<b>Daily Metrics</b><br>%{text}<extra></extra>'
    )])
    
    fig_3d_time.update_layout(
        title='<b>Daily Traffic & Revenue Trend</b>',
        scene=dict(
            xaxis=dict(title='<b>Days</b>'),
            yaxis=dict(title='<b>Sessions</b>'),
            zaxis=dict(title='<b>Revenue (₹)</b>'),
        ),
        height=700,
        template='plotly_white',
        font=dict(family="Arial, sans-serif", size=12, color="#0F3460")
    )
    
    st.plotly_chart(fig_3d_time, use_container_width=True)

# ============================================================================
# TAB 4: PRODUCT CATEGORY 3D
# ============================================================================
with tab4:
    st.markdown("#### Product Category Performance - 3D Analysis")
    
    categories = ['home_appliances', 'office_equipments', 'beauty_products', 'clothing', 'technical_devices']
    
    category_performance = []
    for cat in categories:
        total_views = filtered_df[cat].sum()
        total_purchases = filtered_df[(filtered_df[cat] == 1) & (filtered_df['purchase'] == 1)].shape[0]
        total_revenue = filtered_df[filtered_df[cat] == 1]['order_value'].sum()
        
        category_performance.append({
            'category': cat.replace('_', ' ').title(),
            'views': total_views,
            'purchases': total_purchases,
            'revenue': total_revenue
        })
    
    cat_df = pd.DataFrame(category_performance)
    
    fig_3d_cat = go.Figure(data=[go.Scatter3d(
        x=cat_df['views'],
        y=cat_df['purchases'],
        z=cat_df['revenue'],
        mode='markers+text',
        text=cat_df['category'],
        textposition="top center",
        marker=dict(
            size=12,
            color=['#E94560', '#00D4FF', '#FFB703', '#FF6B6B', '#4ECDC4'],
            opacity=0.85,
            line=dict(width=2, color='white')
        ),
        hovertemplate='<b>%{text}</b><br>Views: %{x}<br>Purchases: %{y}<br>Revenue: ₹%{z:,.0f}<extra></extra>'
    )])
    
    fig_3d_cat.update_layout(
        title='<b>Product Categories: 3D Performance Matrix</b>',
        scene=dict(
            xaxis=dict(title='<b>Total Views</b>'),
            yaxis=dict(title='<b>Total Purchases</b>'),
            zaxis=dict(title='<b>Total Revenue (₹)</b>'),
        ),
        height=700,
        template='plotly_white',
        font=dict(family="Arial, sans-serif", size=12, color="#0F3460")
    )
    
    st.plotly_chart(fig_3d_cat, use_container_width=True)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# ============================================================================
# DETAILED ANALYTICS SECTION
# ============================================================================
st.markdown("### 📊 Detailed Performance Metrics")

col1, col2 = st.columns(2)

# ============================================================================
# Traffic Source Analysis
# ============================================================================
with col1:
    st.markdown("#### Traffic Source Performance")
    
    traffic_stats = filtered_df.groupby('traffic_source').agg({
        'user_id': 'count',
        'purchase': 'sum',
        'order_value': 'sum'
    }).reset_index()
    
    traffic_stats.columns = ['traffic_source', 'sessions', 'purchases', 'revenue']
    traffic_stats = traffic_stats.sort_values('revenue', ascending=False)
    
    fig_traffic = go.Figure()
    
    fig_traffic.add_trace(go.Bar(
        x=traffic_stats['traffic_source'],
        y=traffic_stats['revenue'],
        name='Revenue',
        marker=dict(color='#E94560'),
        text=traffic_stats['revenue'].apply(lambda x: f'₹{x/1000:.0f}K'),
        textposition='outside',
    ))
    
    fig_traffic.update_layout(
        title='<b>Revenue by Traffic Source</b>',
        xaxis_title='Traffic Source',
        yaxis_title='Revenue (₹)',
        height=400,
        template='plotly_white',
        hovermode='x unified',
        font=dict(size=11)
    )
    
    st.plotly_chart(fig_traffic, use_container_width=True)

# ============================================================================
# Device Performance
# ============================================================================
with col2:
    st.markdown("#### Device Type Distribution")
    
    device_stats = filtered_df.groupby('device').agg({
        'user_id': 'count',
        'purchase': 'sum'
    }).reset_index()
    
    device_stats.columns = ['device', 'sessions', 'purchases']
    device_stats['conversion'] = (device_stats['purchases'] / device_stats['sessions'] * 100)
    
    fig_device = go.Figure()
    
    colors = {'Mobile': '#00D4FF', 'Desktop': '#E94560', 'Tablet': '#FFB703'}
    
    fig_device.add_trace(go.Bar(
        x=device_stats['device'],
        y=device_stats['conversion'],
        name='Conversion Rate',
        marker=dict(color=[colors.get(d, '#0F3460') for d in device_stats['device']]),
        text=device_stats['conversion'].apply(lambda x: f'{x:.1f}%'),
        textposition='outside',
    ))
    
    fig_device.update_layout(
        title='<b>Conversion Rate by Device</b>',
        xaxis_title='Device Type',
        yaxis_title='Conversion Rate (%)',
        height=400,
        template='plotly_white',
        showlegend=False,
        font=dict(size=11)
    )
    
    st.plotly_chart(fig_device, use_container_width=True)

col3, col4 = st.columns(2)

# ============================================================================
# Age Group Analysis
# ============================================================================
with col3:
    st.markdown("#### User Age Group Distribution")
    
    filtered_df['age_group'] = pd.cut(filtered_df['age'], 
                                       bins=[0, 20, 30, 40, 50], 
                                       labels=['10-20', '21-30', '31-40', '41-50'])
    
    age_stats = filtered_df.groupby('age_group').agg({
        'user_id': 'count',
        'order_value': 'sum'
    }).reset_index()
    
    age_stats.columns = ['age_group', 'sessions', 'revenue']
    
    fig_age = go.Figure()
    
    fig_age.add_trace(go.Pie(
        labels=age_stats['age_group'],
        values=age_stats['sessions'],
        marker=dict(colors=['#E94560', '#00D4FF', '#FFB703', '#4ECDC4']),
        hole=0.4,
        textposition='inside',
        textinfo='label+percent',
        hovertemplate='<b>%{label}</b><br>Sessions: %{value}<extra></extra>'
    ))
    
    fig_age.update_layout(
        title='<b>Age Group Session Distribution</b>',
        height=400,
        font=dict(size=11)
    )
    
    st.plotly_chart(fig_age, use_container_width=True)

# ============================================================================
# Festival Impact Analysis
# ============================================================================
with col4:
    st.markdown("#### Festival Impact on Revenue")
    
    festival_stats = filtered_df.groupby('festival').agg({
        'order_value': 'sum',
        'user_id': 'count'
    }).reset_index()
    
    festival_stats.columns = ['festival', 'revenue', 'sessions']
    festival_stats = festival_stats.sort_values('revenue', ascending=False)
    
    fig_festival = go.Figure()
    
    fig_festival.add_trace(go.Bar(
        x=festival_stats['festival'],
        y=festival_stats['revenue'],
        name='Revenue',
        marker=dict(color='#FF6B6B'),
        text=festival_stats['revenue'].apply(lambda x: f'₹{x/1000:.0f}K'),
        textposition='outside',
    ))
    
    fig_festival.update_layout(
        title='<b>Revenue by Festival</b>',
        xaxis_title='Festival',
        yaxis_title='Revenue (₹)',
        height=400,
        template='plotly_white',
        showlegend=False,
        font=dict(size=10)
    )
    
    st.plotly_chart(fig_festival, use_container_width=True)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# ============================================================================
# HEATMAP ANALYSIS
# ============================================================================
st.markdown("### 🔥 Correlation Heatmap")

numeric_cols = ['session_duration_sec', 'pages_viewed', 'bounce', 'product_viewed', 
                'add_to_cart', 'purchase', 'order_value', 'age']
corr_matrix = filtered_df[numeric_cols].corr()

fig_heatmap = go.Figure(data=go.Heatmap(
    z=corr_matrix.values,
    x=corr_matrix.columns,
    y=corr_matrix.columns,
    colorscale='RdBu',
    zmid=0,
    text=np.round(corr_matrix.values, 2),
    texttemplate='%{text:.2f}',
    textfont={"size": 10},
    colorbar=dict(title="Correlation")
))

fig_heatmap.update_layout(
    title='<b>Feature Correlation Matrix</b>',
    height=500,
    template='plotly_white',
    font=dict(size=11)
)

st.plotly_chart(fig_heatmap, use_container_width=True)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# ============================================================================
# DATA TABLE SECTION
# ============================================================================
st.markdown("### 📋 Raw Data Preview")

expander = st.expander("View Detailed Data Table", expanded=False)
with expander:
    # Select important columns for display
    display_cols = ['date', 'traffic_source', 'device', 'city', 'session_duration_sec', 
                    'pages_viewed', 'purchase', 'order_value', 'age', 'gender', 'festival']
    
    st.dataframe(
        filtered_df[display_cols].head(100),
        use_container_width=True,
        height=400
    )
    
    st.markdown(f"**Total Records Displayed:** {min(100, len(filtered_df))} of {len(filtered_df)}")

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# ============================================================================
# FOOTER & SUMMARY
# ============================================================================
st.markdown("""
<div style="background: linear-gradient(135deg, #0F3460 0%, #16213E 100%); 
            padding: 30px; border-radius: 12px; color: white; text-align: center; margin-top: 40px;">
    <h3 style="color: white; margin: 0;">📊 E-Commerce Analytics Dashboard</h3>
    <p style="margin: 10px 0 0 0; opacity: 0.9;">
        Data-driven insights for optimizing your e-commerce platform
    </p>
    <hr style="opacity: 0.3; margin: 15px 0;">
    <p style="margin: 0; font-size: 0.9em; opacity: 0.8;">
        🎨 Designed by: <b>i_courner/god</b> | 📅 Updated: 2024
    </p>
</div>
""", unsafe_allow_html=True)
