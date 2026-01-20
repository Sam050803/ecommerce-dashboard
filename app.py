"""
E-commerce Analytics Dashboard
Simple, clean, professional

Ce module déploie un tableau de bord interactif avec Streamlit pour explorer
les données de ventes. Il inclut des filtres latéraux, des KPIs dynamiques
et des visualisations interactives avec Plotly.

Features:
- Chargement des données avec fallback (local vs cloud sample)
- Filtres dynamiques: Pays, Date, Montant min, Top N
- Onglets thématiques: Vue d'ensemble, Analyse temporelle, Export des données
- Support du thème sombre via CSS et configuration Plotly

Author: Seyyid-Aassuf
Date: 2026
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =============================================================================
# CONFIG
# =============================================================================
st.set_page_config(
    page_title="E-commerce Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# SIMPLE CSS
# =============================================================================
st.markdown("""
<style>
    /* Hide footer only - keep header for sidebar toggle */
    footer {visibility: hidden;}
    
    /* Clean layout */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* KPI cards - dark theme compatible */
    div[data-testid="metric-container"] {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 1rem;
        border-radius: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# FUNCTIONS
# =============================================================================
@st.cache_data
def load_data():
    """Load the cleaned e-commerce data. Uses sample file if full data not available."""
    import os
    # Try full data first, fallback to sample for cloud deployment
    full_path = 'data/processed/clean_data.csv'
    sample_path = 'data/processed/clean_data_sample.csv'
    
    if os.path.exists(full_path):
        df = pd.read_csv(full_path, low_memory=False)
    elif os.path.exists(sample_path):
        df = pd.read_csv(sample_path, low_memory=False)
    else:
        st.error("Data file not found. Please ensure clean_data.csv or clean_data_sample.csv exists.")
        st.stop()
    
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    return df

def format_currency(value):
    if value >= 1_000_000:
        return f"£{value/1_000_000:.1f}M"
    elif value >= 1_000:
        return f"£{value/1_000:.0f}K"
    return f"£{value:.0f}"

def format_number(value):
    if value >= 1_000:
        return f"{value/1_000:.0f}K"
    return f"{value:,.0f}"

# =============================================================================
# LOAD DATA
# =============================================================================
df = load_data()

# =============================================================================
# HEADER
# =============================================================================
st.title("E-commerce Analytics Dashboard")
st.markdown('<p class="subtitle">Online Retail UK — December 2010 to December 2011</p>', unsafe_allow_html=True)

# =============================================================================
# SIDEBAR FILTERS
# =============================================================================
# Get default values
min_date = df['InvoiceDate'].min().date()
max_date = df['InvoiceDate'].max().date()

# Check if reset was triggered
if st.session_state.get("reset_triggered", False):
    st.session_state["country_filter"] = "All"
    st.session_state["date_filter"] = (min_date, max_date)
    st.session_state["amount_filter"] = 0
    st.session_state["top_n_filter"] = 10
    st.session_state["reset_triggered"] = False

with st.sidebar:
    st.header("⚙️ Dashboard Settings")
    
    st.subheader("Filters")
    
    # Country
    countries = ["All"] + sorted(df['Country'].unique().tolist())
    if "country_filter" in st.session_state:
        country = st.selectbox("Country", countries, key="country_filter")
    else:
        country = st.selectbox("Country", countries, index=0, key="country_filter")
    
    # Date range
    if "date_filter" in st.session_state:
        date_range = st.date_input(
            "Date Range",
            min_value=min_date,
            max_value=max_date,
            key="date_filter"
        )
    else:
        date_range = st.date_input(
            "Date Range",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date,
            key="date_filter"
        )
    
    # Min amount
    if "amount_filter" in st.session_state:
        min_amount = st.number_input("Min Transaction Amount (£)", min_value=0, step=50, key="amount_filter")
    else:
        min_amount = st.number_input("Min Transaction Amount (£)", min_value=0, value=0, step=50, key="amount_filter")
    
    st.divider()
    st.subheader("Display Options")
    
    # Top N selection
    if "top_n_filter" in st.session_state:
        top_n = st.slider("Number of items in Top charts", min_value=5, max_value=50, step=1, key="top_n_filter")
    else:
        top_n = st.slider("Number of items in Top charts", min_value=5, max_value=50, value=10, step=1, key="top_n_filter")
    
    st.divider()
    
    if st.button("🔄 Reset All", use_container_width=True):
        st.session_state["reset_triggered"] = True
        st.rerun()

# =============================================================================
# DARK THEME CSS
# =============================================================================
st.markdown("""
<style>
    .stApp { background-color: #0e1117; }
    div[data-testid="metric-container"] {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .stTabs [data-baseweb="tab"] { font-size: 1.05rem !important; }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# APPLY FILTERS
# =============================================================================
filtered = df.copy()

if country != "All":
    filtered = filtered[filtered['Country'] == country]

if len(date_range) == 2:
    start, end = date_range
    filtered = filtered[
        (filtered['InvoiceDate'].dt.date >= start) &
        (filtered['InvoiceDate'].dt.date <= end)
    ]

if min_amount > 0:
    tx_totals = filtered.groupby('InvoiceNo')['TotalPrice'].sum()
    valid = tx_totals[tx_totals >= min_amount].index
    filtered = filtered[filtered['InvoiceNo'].isin(valid)]

# Show filter info
if len(filtered) < len(df):
    st.info(f"Showing {len(filtered):,} of {len(df):,} records")

# =============================================================================
# KPIS
# =============================================================================
revenue = filtered['TotalPrice'].sum()
transactions = filtered['InvoiceNo'].nunique()
customers = filtered['CustomerID'].nunique()
avg_basket = revenue / transactions if transactions > 0 else 0

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", format_currency(revenue))
col2.metric("Transactions", format_number(transactions))
col3.metric("Customers", format_number(customers))
col4.metric("Avg Basket", f"£{avg_basket:.0f}")

st.divider()

# =============================================================================
# CHARTS
# =============================================================================

# Common chart config - allow zoom and pan
CHART_CONFIG = {
    'displayModeBar': True,
    'modeBarButtonsToRemove': ['lasso2d', 'select2d', 'autoScale2d'],
    'displaylogo': False
}

def get_layout(dark=True, **kwargs):
    """Returns base layout with theme support"""
    text_color = 'white' if dark else '#333'
    grid_color = 'rgba(255,255,255,0.1)' if dark else '#e0e0e0'
    zero_color = 'rgba(255,255,255,0.2)' if dark else '#cccccc'
    
    base = dict(
        font=dict(family="Arial, sans-serif", size=12, color=text_color),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=40, r=40, t=40, b=60),
        xaxis=dict(
            showgrid=True, 
            gridcolor=grid_color, 
            zeroline=True, 
            zerolinecolor=zero_color,
            tickfont=dict(color=text_color, size=12),
            title=dict(font=dict(color=text_color, size=14))
        ),
        yaxis=dict(
            showgrid=True, 
            gridcolor=grid_color, 
            zeroline=True, 
            zerolinecolor=zero_color,
            tickfont=dict(color=text_color, size=12),
            title=dict(font=dict(color=text_color, size=14))
        )
    )
    base.update(kwargs)
    return base

# Tab navigation
tab1, tab2, tab3 = st.tabs(["Overview", "Time Analysis", "Export"])

with tab1:
    col1, col2 = st.columns(2)
    
    # Revenue by Country
    with col1:
        st.subheader(f"Top {top_n} Countries by Revenue")
        country_data = filtered.groupby('Country')['TotalPrice'].sum().reset_index()
        country_data = country_data.sort_values('TotalPrice', ascending=False).head(top_n)
        
        fig = px.bar(
            country_data,
            x='TotalPrice',
            y='Country',
            orientation='h',
            color_discrete_sequence=['#2563eb'],
            labels={'TotalPrice': 'Revenue (£)', 'Country': 'Country'}
        )
        fig.update_layout(**get_layout(dark=True, 
            height=400, 
            yaxis={'categoryorder':'total ascending'},
            xaxis={'title': {'text': 'Revenue (£)'}},
        ))
        fig.update_traces(hovertemplate='%{y}: %{x:,.0f} £<extra></extra>')
        st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)
    
    # Monthly Revenue
    with col2:
        st.subheader("Monthly Revenue Trend")
        monthly = filtered.groupby('Month')['TotalPrice'].sum().reset_index()
        months = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',
                 7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
        monthly['Month'] = monthly['Month'].map(months)
        
        fig = px.line(
            monthly,
            x='Month',
            y='TotalPrice',
            markers=True,
            color_discrete_sequence=['#10b981'],
            labels={'Month': 'Month', 'TotalPrice': 'Revenue (£)'}
        )
        fig.update_layout(**get_layout(dark=True, 
            height=400,
            xaxis={'title': {'text': 'Month'}},
            yaxis={'title': {'text': 'Revenue (£)'}}
        ))
        fig.update_traces(
            line=dict(width=2),
            marker=dict(size=8),
            hovertemplate='%{x}: %{y:,.0f} £<extra></extra>'
        )
        st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)
    
    col3, col4 = st.columns(2)
    
    # Top Products
    with col3:
        st.subheader(f"Top {top_n} Products")
        products = filtered.groupby('Description')['TotalPrice'].sum().reset_index()
        products = products.sort_values('TotalPrice', ascending=False).head(top_n)
        products['Short'] = products['Description'].str[:30]
        products = products.sort_values('TotalPrice')
        
        fig = px.bar(
            products,
            x='TotalPrice',
            y='Short',
            orientation='h',
            color_discrete_sequence=['#8b5cf6'],
            labels={'TotalPrice': 'Revenue (£)', 'Short': 'Product'},
            custom_data=['Description']
        )
        fig.update_layout(**get_layout(dark=True, 
            height=400, 
            yaxis={'categoryorder':'total ascending'},
            xaxis={'title': {'text': 'Revenue (£)'}}
        ))
        fig.update_traces(hovertemplate='%{customdata[0]}<br>%{y}: %{x:,.0f} £<extra></extra>')
        st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)
    
    # Top Customers
    with col4:
        st.subheader(f"Top {top_n} Customers")
        customers_data = filtered.groupby('CustomerID')['TotalPrice'].sum().reset_index()
        customers_data = customers_data.sort_values('TotalPrice', ascending=False).head(top_n)
        customers_data['ID'] = 'Customer #' + customers_data['CustomerID'].astype(int).astype(str)
        customers_data = customers_data.sort_values('TotalPrice')
        
        fig = px.bar(
            customers_data,
            x='TotalPrice',
            y='ID',
            orientation='h',
            color_discrete_sequence=['#f59e0b'],
            labels={'TotalPrice': 'Revenue (£)', 'ID': 'Customer'}
        )
        fig.update_layout(**get_layout(dark=True, 
            height=400, 
            yaxis={'categoryorder':'total ascending'},
            xaxis={'title': {'text': 'Revenue (£)'}}
        ))
        fig.update_traces(hovertemplate='%{y}: %{x:,.0f} £<extra></extra>')
        st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)

with tab2:
    col1, col2 = st.columns(2)
    
    # Revenue by Day of Week
    with col1:
        st.subheader("Revenue by Day of Week")
        days_order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        day_data = filtered.groupby('DayName')['TotalPrice'].sum().reset_index()
        day_data['Order'] = day_data['DayName'].map({d: i for i, d in enumerate(days_order)})
        day_data = day_data.sort_values('Order')
        
        fig = px.bar(
            day_data,
            x='DayName',
            y='TotalPrice',
            color_discrete_sequence=['#2563eb'],
            labels={'DayName': 'Day of Week', 'TotalPrice': 'Revenue (£)'}
        )
        fig.update_layout(**get_layout(dark=True, 
            height=400,
            xaxis={'title': {'text': 'Day of Week'}},
            yaxis={'title': {'text': 'Revenue (£)'}}
        ))
        fig.update_traces(hovertemplate='%{x}: %{y:,.0f} £<extra></extra>')
        st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)
    
    # Revenue by Hour
    with col2:
        st.subheader("Revenue by Hour")
        hour_data = filtered.groupby('Hour')['TotalPrice'].sum().reset_index()
        
        fig = px.line(
            hour_data,
            x='Hour',
            y='TotalPrice',
            markers=True,
            color_discrete_sequence=['#8b5cf6'],
            labels={'Hour': 'Hour of Day', 'TotalPrice': 'Revenue (£)'}
        )
        fig.update_layout(**get_layout(dark=True, 
            height=400,
            xaxis={'title': {'text': 'Hour of Day'}},
            yaxis={'title': {'text': 'Revenue (£)'}}
        ))
        fig.update_traces(
            line=dict(width=2),
            marker=dict(size=8),
            hovertemplate='Hour %{x}: %{y:,.0f} £<extra></extra>'
        )
        st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)
    
    # Daily trend
    st.subheader("Daily Revenue Evolution")
    daily = filtered.groupby(filtered['InvoiceDate'].dt.date)['TotalPrice'].sum().reset_index()
    daily.columns = ['Date', 'Revenue']
    
    fig = px.line(
        daily,
        x='Date',
        y='Revenue',
        color_discrete_sequence=['#10b981'],
        labels={'Date': 'Date', 'Revenue': 'Revenue (£)'}
    )
    fig.update_layout(**get_layout(dark=True, 
        height=300,
        xaxis={'title': {'text': 'Date'}},
        yaxis={'title': {'text': 'Revenue (£)'}}
    ))
    fig.update_traces(line=dict(width=1.5))
    st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)

with tab3:
    st.subheader("Export Data")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Filtered Data**")
        csv1 = filtered.to_csv(index=False).encode('utf-8')
        st.download_button(
            "Download CSV",
            csv1,
            "filtered_data.csv",
            "text/csv",
            use_container_width=True
        )
        st.caption(f"{len(filtered):,} rows")
    
    with col2:
        st.markdown("**Top Products**")
        top_prod = filtered.groupby('Description')['TotalPrice'].sum().reset_index()
        top_prod = top_prod.sort_values('TotalPrice', ascending=False).head(50)
        csv2 = top_prod.to_csv(index=False).encode('utf-8')
        st.download_button(
            "Download CSV",
            csv2,
            "top_products.csv",
            "text/csv",
            use_container_width=True
        )
        st.caption("Top 50 products")
    
    with col3:
        st.markdown("**Top Customers**")
        top_cust = filtered.groupby('CustomerID').agg({
            'TotalPrice':'sum',
            'InvoiceNo':'nunique'
        }).reset_index()
        top_cust.columns = ['CustomerID','Revenue','Orders']
        top_cust = top_cust.sort_values('Revenue', ascending=False).head(100)
        csv3 = top_cust.to_csv(index=False).encode('utf-8')
        st.download_button(
            "Download CSV",
            csv3,
            "top_customers.csv",
            "text/csv",
            use_container_width=True
        )
        st.caption("Top 100 customers")
    
    st.divider()
    
    st.markdown("**Data Preview**")
    st.dataframe(filtered.head(50), use_container_width=True)
