import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')
 
# ============================================================================
# PAGE CONFIG
# ============================================================================
st.set_page_config(
    page_title="E-Commerce Analytics — India",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)
 
# ============================================================================
# CUSTOM CSS — PROFESSIONAL DARK DASHBOARD
# ============================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500;600&display=swap');
 
    /* ── Global Background ── */
    html, body, [data-testid="stAppViewContainer"] {
        background: #080d1a !important;
        color: #e8eaf0 !important;
    }
    [data-testid="stAppViewContainer"] > .main {
        background: #080d1a !important;
    }
    [data-testid="block-container"] {
        padding-top: 1.5rem !important;
        padding-bottom: 3rem !important;
    }
 
    /* ── Fonts ── */
    *, p, li, span, label, div {
        font-family: 'DM Sans', sans-serif !important;
    }
    h1, h2, h3, h4 {
        font-family: 'Syne', sans-serif !important;
    }
 
    /* ── Sidebar ── */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0d1525 0%, #111827 100%) !important;
        border-right: 1px solid rgba(99, 179, 237, 0.12) !important;
    }
    [data-testid="stSidebar"] .stMarkdown p,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] span {
        color: #94a3b8 !important;
        font-weight: 500 !important;
    }
    [data-testid="stSidebar"] h3 {
        color: #63b3ed !important;
        font-family: 'Syne', sans-serif !important;
        font-size: 1rem !important;
        letter-spacing: 2px !important;
        text-transform: uppercase !important;
    }
    [data-testid="stSidebar"] .stMultiSelect [data-baseweb="tag"] {
        background: rgba(99, 179, 237, 0.2) !important;
        color: #90cdf4 !important;
        border: 1px solid rgba(99, 179, 237, 0.3) !important;
    }
 
    /* ── Header ── */
    .dash-header {
        background: linear-gradient(135deg, #0f1f3d 0%, #1a2d4e 50%, #0f1f3d 100%);
        border: 1px solid rgba(99, 179, 237, 0.2);
        border-radius: 16px;
        padding: 36px 44px;
        margin-bottom: 28px;
        position: relative;
        overflow: hidden;
    }
    .dash-header::before {
        content: '';
        position: absolute;
        top: -60px; right: -60px;
        width: 200px; height: 200px;
        background: radial-gradient(circle, rgba(99,179,237,0.15) 0%, transparent 70%);
        border-radius: 50%;
    }
    .dash-header::after {
        content: '';
        position: absolute;
        bottom: -40px; left: 30%;
        width: 150px; height: 150px;
        background: radial-gradient(circle, rgba(246,135,95,0.1) 0%, transparent 70%);
        border-radius: 50%;
    }
    .dash-header h1 {
        font-family: 'Syne', sans-serif !important;
        font-size: 2.4em !important;
        font-weight: 800 !important;
        color: #ffffff !important;
        margin: 0 !important;
        letter-spacing: -0.5px !important;
    }
    .dash-header p {
        color: #90cdf4 !important;
        font-size: 1em !important;
        margin: 8px 0 0 0 !important;
        opacity: 0.85 !important;
    }
    .dash-header .badge {
        display: inline-block;
        background: rgba(246,135,95,0.15);
        border: 1px solid rgba(246,135,95,0.35);
        color: #f6875f;
        font-size: 0.75em;
        font-weight: 600;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        padding: 4px 12px;
        border-radius: 20px;
        margin-bottom: 10px;
    }
 
    /* ── KPI CARDS — vivid dark glassmorphism ── */
    .kpi-card {
        background: linear-gradient(145deg, #111827 0%, #1a2540 100%);
        border-radius: 14px;
        padding: 24px 22px 20px;
        border: 1px solid rgba(99,179,237,0.15);
        position: relative;
        overflow: hidden;
        transition: transform 0.25s ease, box-shadow 0.25s ease;
        min-height: 130px;
    }
    .kpi-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 40px rgba(0,0,0,0.5);
    }
    .kpi-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 3px;
        border-radius: 14px 14px 0 0;
    }
    .kpi-card.blue::before   { background: linear-gradient(90deg, #63b3ed, #4299e1); }
    .kpi-card.coral::before  { background: linear-gradient(90deg, #f6875f, #ed6b46); }
    .kpi-card.gold::before   { background: linear-gradient(90deg, #fbd38d, #f6ad55); }
    .kpi-card.rose::before   { background: linear-gradient(90deg, #fc8181, #e53e3e); }
 
    .kpi-label {
        font-size: 0.7em !important;
        font-weight: 600 !important;
        letter-spacing: 2px !important;
        text-transform: uppercase !important;
        color: #718096 !important;
        margin-bottom: 10px !important;
        display: block !important;
    }
    .kpi-icon {
        font-size: 1.15em;
        margin-right: 6px;
    }
    .kpi-value {
        font-family: 'Syne', sans-serif !important;
        font-size: 2.2em !important;
        font-weight: 800 !important;
        margin: 0 !important;
        line-height: 1.1 !important;
        letter-spacing: -1px !important;
    }
    .kpi-card.blue  .kpi-value { color: #90cdf4 !important; }
    .kpi-card.coral .kpi-value { color: #f6875f !important; }
    .kpi-card.gold  .kpi-value { color: #fbd38d !important; }
    .kpi-card.rose  .kpi-value { color: #fc8181 !important; }
 
    .kpi-sub {
        font-size: 0.78em !important;
        color: #94a3b8 !important;
        margin-top: 8px !important;
        font-weight: 500 !important;
    }
 
    /* ── Section Titles ── */
    .section-title {
        font-family: 'Syne', sans-serif !important;
        font-size: 1.25em !important;
        font-weight: 700 !important;
        color: #e2e8f0 !important;
        letter-spacing: -0.2px !important;
        padding-bottom: 12px !important;
        border-bottom: 2px solid rgba(99,179,237,0.2) !important;
        margin: 28px 0 20px !important;
    }
 
    /* ── Tabs ── */
    .stTabs [data-baseweb="tab-list"] {
        background: #0d1525 !important;
        border-radius: 10px !important;
        padding: 4px !important;
        gap: 4px !important;
        border: 1px solid rgba(99,179,237,0.12) !important;
    }
    .stTabs [data-baseweb="tab"] {
        color: #718096 !important;
        font-weight: 600 !important;
        font-size: 0.88em !important;
        border-radius: 8px !important;
        padding: 10px 18px !important;
        transition: all 0.2s !important;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #1a3a5c, #0f2744) !important;
        color: #90cdf4 !important;
        border-bottom: none !important;
    }
 
    /* ── Buttons ── */
    .stButton > button {
        background: linear-gradient(135deg, #1a3a5c 0%, #2a4a6c 100%) !important;
        color: #90cdf4 !important;
        border: 1px solid rgba(99,179,237,0.3) !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #2a4a6c, #3a5a7c) !important;
        box-shadow: 0 4px 15px rgba(99,179,237,0.2) !important;
    }
 
    /* ── Expander ── */
    .streamlit-expanderHeader,
    [data-testid="stExpander"] summary,
    [data-testid="stExpander"] > div:first-child {
        background: #111827 !important;
        color: #90cdf4 !important;
        border-radius: 8px !important;
        border: 1px solid rgba(99,179,237,0.15) !important;
        font-weight: 600 !important;
        font-size: 0.92em !important;
        padding: 12px 16px !important;
    }
    [data-testid="stExpander"] summary p,
    [data-testid="stExpander"] summary span {
        color: #90cdf4 !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        white-space: nowrap !important;
    }
    .streamlit-expanderContent,
    [data-testid="stExpander"] > div:last-child {
        background: #0d1525 !important;
        border: 1px solid rgba(99,179,237,0.1) !important;
        border-top: none !important;
        border-radius: 0 0 8px 8px !important;
    }
 
    /* ── Dataframe ── */
    [data-testid="stDataFrame"] {
        background: #111827 !important;
        border-radius: 10px !important;
        border: 1px solid rgba(99,179,237,0.12) !important;
    }
 
    /* ── Info box ── */
    [data-testid="stInfo"] {
        background: rgba(99,179,237,0.08) !important;
        border: 1px solid rgba(99,179,237,0.2) !important;
        color: #90cdf4 !important;
        border-radius: 10px !important;
    }
 
    /* ── Designer credit badge ── */
    .designer-credit {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: linear-gradient(135deg, #1a3a5c 0%, #0f2744 100%);
        color: #90cdf4;
        padding: 10px 18px;
        border-radius: 30px;
        font-weight: 600;
        font-size: 0.82em;
        border: 1px solid rgba(99,179,237,0.25);
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
        z-index: 100;
        letter-spacing: 0.5px;
    }
 
    /* ── Footer ── */
    .dash-footer {
        background: linear-gradient(135deg, #0d1525 0%, #111827 100%);
        border: 1px solid rgba(99,179,237,0.12);
        border-radius: 14px;
        padding: 28px;
        text-align: center;
        margin-top: 40px;
        color: #94a3b8;
    }
    .dash-footer h3 {
        color: #90cdf4 !important;
        margin: 0 0 8px 0 !important;
    }
    .dash-footer p {
        color: #94a3b8 !important;
    }
 
    /* scrollbar */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: #080d1a; }
    ::-webkit-scrollbar-thumb { background: #1a3a5c; border-radius: 3px; }
</style>
""", unsafe_allow_html=True)
 
# ============================================================================
# SHARED PLOTLY THEME  — dark, clean, readable
# ============================================================================
PLOT_BG    = "#0d1525"
PAPER_BG   = "#111827"
GRID_COLOR = "rgba(99,179,237,0.08)"
AXIS_COLOR = "#4a5568"
TICK_COLOR = "#718096"
FONT_COLOR = "#e2e8f0"
ACCENT_COLORS = ["#63b3ed", "#f6875f", "#fbd38d", "#68d391", "#fc8181", "#b794f4"]
 
def dark_layout(fig, title="", height=500, scene3d=False):
    """Apply consistent dark theme to any plotly figure."""
    fig.update_layout(
        title=dict(text=f"<b>{title}</b>", font=dict(color=FONT_COLOR, size=14, family="Syne"), x=0.02),
        paper_bgcolor=PAPER_BG,
        plot_bgcolor=PLOT_BG,
        font=dict(family="DM Sans, sans-serif", color=TICK_COLOR, size=11),
        height=height,
        margin=dict(l=12, r=12, t=50, b=12),
        legend=dict(
            bgcolor="rgba(13,21,37,0.8)",
            bordercolor="rgba(99,179,237,0.15)",
            borderwidth=1,
            font=dict(color=TICK_COLOR),
        ),
        hovermode="x unified",
    )
    if not scene3d:
        fig.update_xaxes(
            gridcolor=GRID_COLOR, linecolor=AXIS_COLOR, tickfont=dict(color=TICK_COLOR),
            title_font=dict(color=TICK_COLOR), zeroline=False
        )
        fig.update_yaxes(
            gridcolor=GRID_COLOR, linecolor=AXIS_COLOR, tickfont=dict(color=TICK_COLOR),
            title_font=dict(color=TICK_COLOR), zeroline=False
        )
    return fig
 
def apply_3d_layout(fig, title, xlabel, ylabel, zlabel, height=500):
    """Apply dark 3D layout with labelled axes to any 3D figure."""
    sc = dark_scene()
    sc['xaxis']['title'] = xlabel
    sc['yaxis']['title'] = ylabel
    sc['zaxis']['title'] = zlabel
    fig.update_layout(
        title=dict(text=f"<b>{title}</b>",
                   font=dict(color=FONT_COLOR, size=14, family="Syne"), x=0.02),
        scene=sc,
        paper_bgcolor=PAPER_BG,
        font=dict(color=TICK_COLOR),
        height=height,
        margin=dict(l=0, r=0, b=0, t=50),
    )
    return fig
 
def make_3d_bars(categories, values, colors, xlabel="Category", ylabel="Index",
                 zlabel="Value", width=0.4):
    """
    Build a 3D bar chart by drawing a filled mesh (box) per category.
    categories : list of str labels
    values      : list of numeric heights (z)
    colors      : list of colour strings (one per bar)
    Returns a go.Figure.
    """
    fig = go.Figure()
    for i, (cat, val, col) in enumerate(zip(categories, values, colors)):
        x0, x1 = i - width / 2, i + width / 2
        y0, y1 = -width / 2, width / 2
        z0, z1 = 0, val
        # 6 faces of a rectangular box
        verts_x = [x0,x1,x1,x0, x0,x1,x1,x0]
        verts_y = [y0,y0,y1,y1, y0,y0,y1,y1]
        verts_z = [z0,z0,z0,z0, z1,z1,z1,z1]
        i_idx = [0,0,0,4,4,4,0,2,1,5,7,6]
        j_idx = [1,2,3,5,6,7,4,6,5,1,3,2]
        k_idx = [2,3,0,6,7,4,5,7,6,2,0,3]
        fig.add_trace(go.Mesh3d(
            x=verts_x, y=verts_y, z=verts_z,
            i=i_idx, j=j_idx, k=k_idx,
            color=col,
            opacity=0.88,
            name=cat,
            hovertemplate=f"<b>{cat}</b><br>{zlabel}: {val:,.0f}<extra></extra>",
            showscale=False,
            flatshading=True,
            lighting=dict(ambient=0.6, diffuse=0.8, specular=0.3, roughness=0.5),
            lightposition=dict(x=100, y=200, z=150),
        ))
        # top label
        fig.add_trace(go.Scatter3d(
            x=[(x0+x1)/2], y=[0], z=[z1 * 1.05],
            mode='text',
            text=[cat],
            textfont=dict(color="#e2e8f0", size=9),
            showlegend=False,
            hoverinfo='skip',
        ))
    # tick positions on x-axis
    sc = dark_scene()
    sc['xaxis']['title'] = xlabel
    sc['xaxis']['tickvals'] = list(range(len(categories)))
    sc['xaxis']['ticktext'] = [''] * len(categories)   # labels shown as Scatter3d text
    sc['yaxis']['title'] = ylabel
    sc['yaxis']['showticklabels'] = False
    sc['zaxis']['title'] = zlabel
    fig.update_layout(scene=sc, paper_bgcolor=PAPER_BG,
                      font=dict(color=TICK_COLOR), showlegend=False)
    return fig
 
def dark_scene():
    """Return a Plotly scene dict with correct dark 3D styling."""
    axis_style = dict(
        backgroundcolor="#0d1525",
        gridcolor="rgba(99,179,237,0.15)",
        linecolor="rgba(99,179,237,0.3)",
        tickfont=dict(color="#94a3b8", size=10),
        title=dict(font=dict(color="#90cdf4", size=12, family="DM Sans")),
        showbackground=True,
        zerolinecolor="rgba(99,179,237,0.2)",
    )
    return dict(
        xaxis=dict(**axis_style),
        yaxis=dict(**axis_style),
        zaxis=dict(**axis_style),
        bgcolor="#080d1a",
        camera=dict(eye=dict(x=1.6, y=1.6, z=1.2)),
    )
 
# ============================================================================
# LOAD AND PREPARE DATA
# ============================================================================
@st.cache_data
def load_data():
    df = pd.read_excel('Ecommerce_Website_Traffic_India.xlsx')
 
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    df = df.drop_duplicates()
    df = df.dropna(subset=['user_id', 'time'])
 
    df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce')
    df = df.dropna(subset=['date'])
 
    numeric_cols = df.select_dtypes(include=np.number).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
 
    return df
 
df = load_data()
 
# ============================================================================
# SIDEBAR FILTERS
# ============================================================================
st.sidebar.markdown("### 🎯  FILTERS")
st.sidebar.markdown("---")
 
date_range = st.sidebar.date_input(
    "📅 Date Range",
    value=(df['date'].min(), df['date'].max()),
    min_value=df['date'].min(),
    max_value=df['date'].max()
)
 
traffic_sources = st.sidebar.multiselect(
    "🔗 Traffic Source",
    options=sorted(df['traffic_source'].unique()),
    default=df['traffic_source'].unique()
)
 
devices = st.sidebar.multiselect(
    "📱 Device Type",
    options=sorted(df['device'].unique()),
    default=df['device'].unique()
)
 
festivals = st.sidebar.multiselect(
    "🎉 Festival",
    options=sorted(df['festival'].unique()),
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
<div class="dash-header">
    <div class="badge">India E-Commerce · Live Analytics</div>
    <h1>📊 E-Commerce Traffic Analytics</h1>
    <p>Advanced insights into India's e-commerce website traffic patterns &amp; user behaviour</p>
</div>
""", unsafe_allow_html=True)
 
st.markdown("""<div class="designer-credit">🎨 Designer: Ankit</div>""", unsafe_allow_html=True)
 
# ============================================================================
# KPI CARDS
# ============================================================================
st.markdown('<p class="section-title">📈 Key Performance Indicators</p>', unsafe_allow_html=True)
 
col1, col2, col3, col4 = st.columns(4)
 
with col1:
    st.markdown(f"""
    <div class="kpi-card blue">
        <span class="kpi-label"><span class="kpi-icon">👥</span>Total Sessions</span>
        <p class="kpi-value">{len(filtered_df):,}</p>
        <p class="kpi-sub">Active user sessions</p>
    </div>""", unsafe_allow_html=True)
 
with col2:
    conversion_rate = (filtered_df['purchase'].sum() / len(filtered_df)) * 100
    st.markdown(f"""
    <div class="kpi-card coral">
        <span class="kpi-label"><span class="kpi-icon">🎯</span>Conversion Rate</span>
        <p class="kpi-value">{conversion_rate:.2f}%</p>
        <p class="kpi-sub">Purchase conversion</p>
    </div>""", unsafe_allow_html=True)
 
with col3:
    avg_order_value = filtered_df['order_value'].mean()
    st.markdown(f"""
    <div class="kpi-card gold">
        <span class="kpi-label"><span class="kpi-icon">💰</span>Avg Order Value</span>
        <p class="kpi-value">₹{avg_order_value:,.0f}</p>
        <p class="kpi-sub">Average revenue per order</p>
    </div>""", unsafe_allow_html=True)
 
with col4:
    bounce_rate = (filtered_df['bounce'].sum() / len(filtered_df)) * 100
    st.markdown(f"""
    <div class="kpi-card rose">
        <span class="kpi-label"><span class="kpi-icon">📉</span>Bounce Rate</span>
        <p class="kpi-value">{bounce_rate:.2f}%</p>
        <p class="kpi-sub">Session exits without action</p>
    </div>""", unsafe_allow_html=True)
 
st.markdown("<br>", unsafe_allow_html=True)
 
# ============================================================================
# 3D VISUALIZATIONS
# ============================================================================
st.markdown('<p class="section-title">🎨 Advanced 3D Analytics</p>', unsafe_allow_html=True)
 
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 3D Scatter Analysis",
    "🗺️ Geographic 3D",
    "⏰ Time Series 3D",
    "🛍️ Product Category 3D"
])
 
# ── TAB 1 ──
with tab1:
    col_left, col_right = st.columns([3, 1])
    with col_left:
        sample = filtered_df.sample(min(3000, len(filtered_df)), random_state=42)
        fig_3d_scatter = go.Figure(data=[go.Scatter3d(
            x=sample['session_duration_sec'],
            y=sample['pages_viewed'],
            z=sample['order_value'],
            mode='markers',
            marker=dict(
                size=sample['order_value'].apply(lambda x: max(3, min(10, x / 200))),
                color=sample['order_value'],
                colorscale='Turbo',
                colorbar=dict(
                    title=dict(text="Order Value (₹)", font=dict(color="#94a3b8", size=11)),
                    tickfont=dict(color="#94a3b8"),
                    bgcolor=PAPER_BG,
                    bordercolor="rgba(99,179,237,0.2)",
                    thickness=14, len=0.65
                ),
                opacity=0.85,
                line=dict(width=0)
            ),
            text=[f"Duration: {d}s | Pages: {p} | Value: ₹{v:.0f} | Device: {dv}"
                  for d, p, v, dv in zip(sample['session_duration_sec'],
                                         sample['pages_viewed'],
                                         sample['order_value'],
                                         sample['device'])],
            hovertemplate='<b>Session Details</b><br>%{text}<extra></extra>'
        )])
 
        scene = dark_scene()
        scene['xaxis']['title'] = 'Session Duration (seconds)'
        scene['yaxis']['title'] = 'Pages Viewed'
        scene['zaxis']['title'] = 'Order Value (₹)'
 
        fig_3d_scatter.update_layout(
            title=dict(text="<b>Session Duration × Pages Viewed × Order Value</b>",
                       font=dict(color=FONT_COLOR, size=14, family="Syne"), x=0.02),
            scene=scene,
            paper_bgcolor=PAPER_BG,
            font=dict(color=TICK_COLOR),
            height=600,
            margin=dict(l=0, r=0, b=0, t=50),
        )
        st.plotly_chart(fig_3d_scatter, use_container_width=True)
 
    with col_right:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.info("""
**Key Findings:**
 
🎯 Higher page views → higher order values
 
⏱️ Session duration positively correlates with purchases
 
💡 Optimise user journey to increase pages viewed
 
🔍 Focus on reducing bounce for high-value products
        """)
 
# ── TAB 2 ──
with tab2:
    state_data = filtered_df.groupby('state').agg(
        total_value=('order_value', 'sum'),
        sessions=('user_id', 'count'),
        purchases=('purchase', 'sum')
    ).reset_index().sort_values('total_value', ascending=False).head(15)
 
    fig_3d_geo = go.Figure(data=[go.Scatter3d(
        x=state_data['sessions'],
        y=state_data['purchases'],
        z=state_data['total_value'],
        mode='markers+text',
        text=state_data['state'],
        textfont=dict(color="#90cdf4", size=10),
        textposition="top center",
        marker=dict(
            size=state_data['total_value'].apply(lambda x: max(5, min(20, x / 1000))),
            color=state_data['total_value'],
            colorscale='Plasma',
            colorbar=dict(
                title=dict(text="Revenue (₹)", font=dict(color="#94a3b8", size=11)),
                tickfont=dict(color="#94a3b8"),
                bgcolor=PAPER_BG,
                bordercolor="rgba(99,179,237,0.2)",
                thickness=14, len=0.65
            ),
            opacity=0.9,
            line=dict(width=1, color='rgba(255,255,255,0.3)')
        ),
        hovertemplate='<b>%{text}</b><br>Sessions: %{x}<br>Purchases: %{y}<br>Revenue: ₹%{z:,.0f}<extra></extra>'
    )])
 
    scene2 = dark_scene()
    scene2['xaxis']['title'] = 'Total Sessions'
    scene2['yaxis']['title'] = 'Total Purchases'
    scene2['zaxis']['title'] = 'Total Revenue (₹)'
 
    fig_3d_geo.update_layout(
        title=dict(text="<b>Top 15 States — 3D Revenue Analysis</b>",
                   font=dict(color=FONT_COLOR, size=14, family="Syne"), x=0.02),
        scene=scene2,
        paper_bgcolor=PAPER_BG,
        font=dict(color=TICK_COLOR),
        height=700,
        margin=dict(l=0, r=0, b=0, t=50),
    )
    st.plotly_chart(fig_3d_geo, use_container_width=True)
 
# ── TAB 3 ──
with tab3:
    daily_data = filtered_df.groupby(filtered_df['date'].dt.date).agg(
        sessions=('user_id', 'count'),
        revenue=('order_value', 'sum'),
        purchases=('purchase', 'sum')
    ).reset_index()
    daily_data.columns = ['date', 'sessions', 'revenue', 'purchases']
    daily_data['date_num'] = range(len(daily_data))
 
    fig_3d_time = go.Figure(data=[go.Scatter3d(
        x=daily_data['date_num'],
        y=daily_data['sessions'],
        z=daily_data['revenue'],
        mode='markers+lines',
        marker=dict(
            size=daily_data['purchases'].apply(lambda x: max(4, min(12, x / 2))),
            color=daily_data['revenue'],
            colorscale='Viridis',
            colorbar=dict(
                title=dict(text="Revenue (₹)", font=dict(color="#94a3b8", size=11)),
                tickfont=dict(color="#94a3b8"),
                bgcolor=PAPER_BG,
                bordercolor="rgba(99,179,237,0.2)",
                thickness=14, len=0.65
            ),
            opacity=0.85
        ),
        line=dict(color='rgba(99,179,237,0.5)', width=2),
        text=[f"Date: {d} | Sessions: {s} | Revenue: ₹{r:,.0f} | Purchases: {p}"
              for d, s, r, p in zip(daily_data['date'], daily_data['sessions'],
                                    daily_data['revenue'], daily_data['purchases'])],
        hovertemplate='<b>Daily Metrics</b><br>%{text}<extra></extra>'
    )])
 
    scene3 = dark_scene()
    scene3['xaxis']['title'] = 'Day Number'
    scene3['yaxis']['title'] = 'Sessions'
    scene3['zaxis']['title'] = 'Revenue (₹)'
 
    fig_3d_time.update_layout(
        title=dict(text="<b>Daily Traffic & Revenue Trend</b>",
                   font=dict(color=FONT_COLOR, size=14, family="Syne"), x=0.02),
        scene=scene3,
        paper_bgcolor=PAPER_BG,
        font=dict(color=TICK_COLOR),
        height=700,
        margin=dict(l=0, r=0, b=0, t=50),
    )
    st.plotly_chart(fig_3d_time, use_container_width=True)
 
# ── TAB 4 ──
with tab4:
    categories = ['home_appliances', 'office_equipments', 'beauty_products', 'clothing', 'technical_devices']
    cat_rows = []
    for cat in categories:
        cat_rows.append({
            'category': cat.replace('_', ' ').title(),
            'views': int(filtered_df[cat].sum()),
            'purchases': int(filtered_df[(filtered_df[cat] == 1) & (filtered_df['purchase'] == 1)].shape[0]),
            'revenue': float(filtered_df[filtered_df[cat] == 1]['order_value'].sum())
        })
    cat_df = pd.DataFrame(cat_rows)
 
    fig_3d_cat = go.Figure(data=[go.Scatter3d(
        x=cat_df['views'],
        y=cat_df['purchases'],
        z=cat_df['revenue'],
        mode='markers+text',
        text=cat_df['category'],
        textfont=dict(color="#fbd38d", size=11),
        textposition="top center",
        marker=dict(
            size=12,
            color=ACCENT_COLORS[:5],
            opacity=0.9,
            line=dict(width=2, color='rgba(255,255,255,0.4)')
        ),
        hovertemplate='<b>%{text}</b><br>Views: %{x}<br>Purchases: %{y}<br>Revenue: ₹%{z:,.0f}<extra></extra>'
    )])
 
    scene4 = dark_scene()
    scene4['xaxis']['title'] = 'Total Views'
    scene4['yaxis']['title'] = 'Total Purchases'
    scene4['zaxis']['title'] = 'Total Revenue (₹)'
 
    fig_3d_cat.update_layout(
        title=dict(text="<b>Product Categories — 3D Performance Matrix</b>",
                   font=dict(color=FONT_COLOR, size=14, family="Syne"), x=0.02),
        scene=scene4,
        paper_bgcolor=PAPER_BG,
        font=dict(color=TICK_COLOR),
        height=700,
        margin=dict(l=0, r=0, b=0, t=50),
    )
    st.plotly_chart(fig_3d_cat, use_container_width=True)
 
st.markdown("<br>", unsafe_allow_html=True)
 
# ============================================================================
# DETAILED ANALYTICS SECTION
# ============================================================================
st.markdown('<p class="section-title">📊 Detailed Performance Metrics</p>', unsafe_allow_html=True)
 
col1, col2 = st.columns(2)
 
# Traffic Source — 3D Bar
with col1:
    traffic_stats = filtered_df.groupby('traffic_source').agg(
        sessions=('user_id', 'count'),
        purchases=('purchase', 'sum'),
        revenue=('order_value', 'sum')
    ).reset_index().sort_values('revenue', ascending=False)
 
    fig_traffic = go.Figure()
    colors_t = ACCENT_COLORS[:len(traffic_stats)]
    for i, (_, row) in enumerate(traffic_stats.iterrows()):
        w = 0.35
        x0, x1 = i - w/2, i + w/2
        y0, y1 = -w/2, w/2
        z1 = row['revenue']
        vx = [x0,x1,x1,x0, x0,x1,x1,x0]
        vy = [y0,y0,y1,y1, y0,y0,y1,y1]
        vz = [0,0,0,0, z1,z1,z1,z1]
        fig_traffic.add_trace(go.Mesh3d(
            x=vx, y=vy, z=vz,
            i=[0,0,0,4,4,4,0,2,1,5,7,6],
            j=[1,2,3,5,6,7,4,6,5,1,3,2],
            k=[2,3,0,6,7,4,5,7,6,2,0,3],
            color=colors_t[i], opacity=0.88, flatshading=True,
            lighting=dict(ambient=0.6, diffuse=0.8, specular=0.3),
            hovertemplate=f"<b>{row['traffic_source']}</b><br>Revenue: ₹{z1:,.0f}<br>Sessions: {row['sessions']:,}<extra></extra>",
            showscale=False, showlegend=False,
        ))
        fig_traffic.add_trace(go.Scatter3d(
            x=[(x0+x1)/2], y=[0], z=[z1 * 1.06],
            mode='text', text=[row['traffic_source']],
            textfont=dict(color="#e2e8f0", size=8),
            showlegend=False, hoverinfo='skip',
        ))
    sc_t = dark_scene()
    sc_t['xaxis']['title'] = 'Traffic Source'
    sc_t['xaxis']['showticklabels'] = False
    sc_t['yaxis']['title'] = ''
    sc_t['yaxis']['showticklabels'] = False
    sc_t['zaxis']['title'] = 'Revenue (₹)'
    fig_traffic.update_layout(
        title=dict(text="<b>Revenue by Traffic Source</b>",
                   font=dict(color=FONT_COLOR, size=14, family="Syne"), x=0.02),
        scene=sc_t, paper_bgcolor=PAPER_BG,
        font=dict(color=TICK_COLOR), height=450,
        margin=dict(l=0, r=0, b=0, t=50), showlegend=False,
    )
    st.plotly_chart(fig_traffic, use_container_width=True)
 
# Device Performance — 3D Bar
with col2:
    device_stats = filtered_df.groupby('device').agg(
        sessions=('user_id', 'count'),
        purchases=('purchase', 'sum')
    ).reset_index()
    device_stats['conversion'] = (device_stats['purchases'] / device_stats['sessions'] * 100)
 
    color_map = {'Mobile': '#63b3ed', 'Desktop': '#f6875f', 'Tablet': '#fbd38d'}
    fig_device = go.Figure()
    for i, (_, row) in enumerate(device_stats.iterrows()):
        w = 0.4
        x0, x1 = i - w/2, i + w/2
        y0, y1 = -w/2, w/2
        z1 = row['conversion']
        col_d = color_map.get(row['device'], '#68d391')
        vx = [x0,x1,x1,x0, x0,x1,x1,x0]
        vy = [y0,y0,y1,y1, y0,y0,y1,y1]
        vz = [0,0,0,0, z1,z1,z1,z1]
        fig_device.add_trace(go.Mesh3d(
            x=vx, y=vy, z=vz,
            i=[0,0,0,4,4,4,0,2,1,5,7,6],
            j=[1,2,3,5,6,7,4,6,5,1,3,2],
            k=[2,3,0,6,7,4,5,7,6,2,0,3],
            color=col_d, opacity=0.88, flatshading=True,
            lighting=dict(ambient=0.6, diffuse=0.8, specular=0.3),
            hovertemplate=f"<b>{row['device']}</b><br>Conversion: {z1:.1f}%<br>Sessions: {row['sessions']:,}<extra></extra>",
            showscale=False, showlegend=False,
        ))
        fig_device.add_trace(go.Scatter3d(
            x=[(x0+x1)/2], y=[0], z=[z1 * 1.06],
            mode='text', text=[f"{row['device']}<br>{z1:.1f}%"],
            textfont=dict(color="#e2e8f0", size=9),
            showlegend=False, hoverinfo='skip',
        ))
    sc_d = dark_scene()
    sc_d['xaxis']['title'] = 'Device Type'
    sc_d['xaxis']['showticklabels'] = False
    sc_d['yaxis']['title'] = ''
    sc_d['yaxis']['showticklabels'] = False
    sc_d['zaxis']['title'] = 'Conversion Rate (%)'
    fig_device.update_layout(
        title=dict(text="<b>Conversion Rate by Device</b>",
                   font=dict(color=FONT_COLOR, size=14, family="Syne"), x=0.02),
        scene=sc_d, paper_bgcolor=PAPER_BG,
        font=dict(color=TICK_COLOR), height=450,
        margin=dict(l=0, r=0, b=0, t=50), showlegend=False,
    )
    st.plotly_chart(fig_device, use_container_width=True)
 
col3, col4 = st.columns(2)
 
# Age Group — 3D Bubble Scatter
with col3:
    filtered_df['age_group'] = pd.cut(
        filtered_df['age'],
        bins=[0, 20, 30, 40, 60],
        labels=['Under 20', '21–30', '31–40', '41+']
    )
    age_stats = filtered_df.groupby('age_group', observed=True).agg(
        sessions=('user_id', 'count'),
        revenue=('order_value', 'sum'),
        purchases=('purchase', 'sum')
    ).reset_index()
    age_stats['conversion'] = age_stats['purchases'] / age_stats['sessions'] * 100
 
    fig_age = go.Figure(data=[go.Scatter3d(
        x=list(range(len(age_stats))),
        y=age_stats['sessions'],
        z=age_stats['revenue'],
        mode='markers+text',
        text=age_stats['age_group'].astype(str),
        textfont=dict(color="#e2e8f0", size=10),
        textposition="top center",
        marker=dict(
            size=age_stats['conversion'].apply(lambda x: max(10, min(30, x * 3))),
            color=ACCENT_COLORS[:4],
            opacity=0.9,
            line=dict(width=2, color='rgba(255,255,255,0.3)'),
            symbol='circle',
        ),
        hovertemplate='<b>%{text}</b><br>Sessions: %{y:,}<br>Revenue: ₹%{z:,.0f}<extra></extra>'
    )])
    sc_a = dark_scene()
    sc_a['xaxis']['title'] = 'Age Group'
    sc_a['xaxis']['tickvals'] = list(range(len(age_stats)))
    sc_a['xaxis']['ticktext'] = age_stats['age_group'].astype(str).tolist()
    sc_a['yaxis']['title'] = 'Sessions'
    sc_a['zaxis']['title'] = 'Revenue (₹)'
    fig_age.update_layout(
        title=dict(text="<b>Age Group — Sessions & Revenue</b>",
                   font=dict(color=FONT_COLOR, size=14, family="Syne"), x=0.02),
        scene=sc_a, paper_bgcolor=PAPER_BG,
        font=dict(color=TICK_COLOR), height=450,
        margin=dict(l=0, r=0, b=0, t=50),
    )
    st.plotly_chart(fig_age, use_container_width=True)
 
# Festival Impact — 3D Bar
with col4:
    festival_stats = filtered_df.groupby('festival').agg(
        revenue=('order_value', 'sum'),
        sessions=('user_id', 'count')
    ).reset_index().sort_values('revenue', ascending=False)
 
    fig_festival = go.Figure()
    colors_f = ACCENT_COLORS * 3   # repeat if more festivals than accent colours
    for i, (_, row) in enumerate(festival_stats.iterrows()):
        w = 0.38
        x0, x1 = i - w/2, i + w/2
        y0, y1 = -w/2, w/2
        z1 = row['revenue']
        vx = [x0,x1,x1,x0, x0,x1,x1,x0]
        vy = [y0,y0,y1,y1, y0,y0,y1,y1]
        vz = [0,0,0,0, z1,z1,z1,z1]
        fig_festival.add_trace(go.Mesh3d(
            x=vx, y=vy, z=vz,
            i=[0,0,0,4,4,4,0,2,1,5,7,6],
            j=[1,2,3,5,6,7,4,6,5,1,3,2],
            k=[2,3,0,6,7,4,5,7,6,2,0,3],
            color=colors_f[i % len(colors_f)], opacity=0.88, flatshading=True,
            lighting=dict(ambient=0.6, diffuse=0.8, specular=0.3),
            hovertemplate=f"<b>{row['festival']}</b><br>Revenue: ₹{z1:,.0f}<br>Sessions: {row['sessions']:,}<extra></extra>",
            showscale=False, showlegend=False,
        ))
        fig_festival.add_trace(go.Scatter3d(
            x=[(x0+x1)/2], y=[0], z=[z1 * 1.05],
            mode='text', text=[row['festival']],
            textfont=dict(color="#e2e8f0", size=8),
            showlegend=False, hoverinfo='skip',
        ))
    sc_f = dark_scene()
    sc_f['xaxis']['title'] = 'Festival'
    sc_f['xaxis']['showticklabels'] = False
    sc_f['yaxis']['title'] = ''
    sc_f['yaxis']['showticklabels'] = False
    sc_f['zaxis']['title'] = 'Revenue (₹)'
    fig_festival.update_layout(
        title=dict(text="<b>Revenue by Festival</b>",
                   font=dict(color=FONT_COLOR, size=14, family="Syne"), x=0.02),
        scene=sc_f, paper_bgcolor=PAPER_BG,
        font=dict(color=TICK_COLOR), height=450,
        margin=dict(l=0, r=0, b=0, t=50), showlegend=False,
    )
    st.plotly_chart(fig_festival, use_container_width=True)
 
st.markdown("<br>", unsafe_allow_html=True)
 
# ============================================================================
# CORRELATION HEATMAP
# ============================================================================
st.markdown('<p class="section-title">🔥 Correlation — 3D Surface</p>', unsafe_allow_html=True)
 
numeric_cols = ['session_duration_sec', 'pages_viewed', 'bounce', 'product_viewed',
                'add_to_cart', 'purchase', 'order_value', 'age']
corr_matrix = filtered_df[numeric_cols].corr()
 
# Build 3D surface from correlation matrix
fig_heatmap = go.Figure(data=[go.Surface(
    z=corr_matrix.values,
    x=corr_matrix.columns.tolist(),
    y=corr_matrix.columns.tolist(),
    colorscale='RdBu',
    cmid=0,
    cmin=-1, cmax=1,
    colorbar=dict(
        title=dict(text="Correlation", font=dict(color="#94a3b8", size=11)),
        tickfont=dict(color="#94a3b8"),
        bgcolor=PAPER_BG,
        bordercolor="rgba(99,179,237,0.2)",
        thickness=14, len=0.65,
    ),
    opacity=0.92,
    contours=dict(
        z=dict(show=True, usecolormap=True, highlightcolor="#90cdf4", project_z=True)
    ),
    hovertemplate='<b>%{x}</b> × <b>%{y}</b><br>Correlation: %{z:.2f}<extra></extra>',
)])
 
sc_hm = dark_scene()
sc_hm['xaxis']['title'] = 'Feature'
sc_hm['yaxis']['title'] = 'Feature'
sc_hm['zaxis']['title'] = 'Correlation'
sc_hm['xaxis']['tickangle'] = -25
sc_hm['camera'] = dict(eye=dict(x=1.8, y=1.8, z=1.4))
 
fig_heatmap.update_layout(
    title=dict(text="<b>Feature Correlation — 3D Surface</b>",
               font=dict(color=FONT_COLOR, size=14, family="Syne"), x=0.02),
    scene=sc_hm,
    paper_bgcolor=PAPER_BG,
    font=dict(color=TICK_COLOR),
    height=600,
    margin=dict(l=0, r=0, b=0, t=50),
)
 
st.plotly_chart(fig_heatmap, use_container_width=True)
 
st.markdown("<br>", unsafe_allow_html=True)
 
# ============================================================================
# DATA TABLE
# ============================================================================
st.markdown('<p class="section-title">📋 Raw Data Preview</p>', unsafe_allow_html=True)
 
with st.expander ("View Detailed Data Table", expanded=False):
    display_cols = ['date', 'traffic_source', 'device', 'city', 'state',
                    'session_duration_sec', 'pages_viewed', 'purchase',
                    'order_value', 'age', 'gender', 'festival']
    st.dataframe(
        filtered_df[display_cols].head(100),
        use_container_width=True,
        height=400
    )
    st.markdown(f"**Total Records Displayed:** {min(100, len(filtered_df)):,} of {len(filtered_df):,}")
 
# ============================================================================
# FOOTER
# ============================================================================
st.markdown("""
<div class="dash-footer">
    <h3>📊 E-Commerce Analytics Dashboard</h3>
    <p style="color:#94a3b8; margin:6px 0 0 0;">Data-driven insights for optimising your e-commerce platform</p>
    <hr style="border:none; border-top:1px solid rgba(99,179,237,0.1); margin:16px 0;">
    <p style="margin:0; font-size:0.85em; color:#94a3b8;">
        🎨 Designed by: <b style="color:#90cdf4;">Ankit</b> &nbsp;|&nbsp; 📅 Updated: 2024
    </p>
</div>
""", unsafe_allow_html=True)
 
