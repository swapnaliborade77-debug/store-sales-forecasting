import streamlit as st
import pickle
import numpy as np
from datetime import datetime

# ── Page Config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Rossmann · Sales Forecast",
    page_icon="🔵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Sky Blue Theme CSS ─────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
    --sky-50:   #f0f9ff;
    --sky-100:  #e0f2fe;
    --sky-200:  #bae6fd;
    --sky-300:  #7dd3fc;
    --sky-400:  #38bdf8;
    --sky-500:  #0ea5e9;
    --sky-600:  #0284c7;
    --sky-700:  #0369a1;
    --sky-800:  #075985;
    --sky-900:  #0c4a6e;
    --white:      #ffffff;
    --bg:          #f0f9ff;
    --text-dark:  #0c4a6e;
    --text-mid:   #0369a1;
    --text-soft:  #0ea5e9;
    --text-muted: #7dd3fc;
    --border:      rgba(2,132,199,0.14);
    --shadow-sm:  rgba(2,132,199,0.08);
    --shadow-md:  rgba(2,132,199,0.18);
    --glow:        rgba(14,165,233,0.20);
}

*, *::before, *::after { box-sizing: border-box; }

html, body, .stApp {
    background: var(--bg) !important;
    font-family: 'Inter', sans-serif !important;
    color: var(--text-dark) !important;
}

#MainMenu, footer, header { visibility: hidden !important; }
.block-container { padding: 0 2rem 4rem !important; max-width: 1180px !important; }

/* ── NAVBAR ── */
.navbar {
    background: var(--white);
    border-bottom: 1px solid var(--border);
    padding: 0 28px;
    height: 58px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin: 0 -2rem 0;
}
.navbar-brand { display: flex; align-items: center; gap: 10px; }
.brand-icon {
    width: 34px; height: 34px;
    background: var(--sky-600);
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 17px;
}
.brand-name { font-size: 16px; font-weight: 700; color: var(--text-dark); letter-spacing: -0.3px; }
.brand-name span { color: var(--sky-600); }
.navbar-right { display: flex; align-items: center; gap: 8px; }
.nav-chip {
    font-size: 11px; font-weight: 600; letter-spacing: 0.3px;
    padding: 4px 12px; border-radius: 20px;
    border: 1px solid var(--sky-200);
    background: var(--sky-50); color: var(--sky-700);
}
.nav-chip.live { background: #f0fdf4; color: #15803d; border-color: #bbf7d0; }

/* ── HERO ── */
.hero {
    background: var(--sky-700);
    border-radius: 22px;
    margin: 26px 0 30px;
    padding: 50px 52px 46px;
    position: relative;
    overflow: hidden;
}
.hero-circle-1 {
    position: absolute; top: -90px; right: -90px;
    width: 340px; height: 340px; border-radius: 50%;
    background: rgba(255,255,255,0.05); pointer-events: none;
}
.hero-circle-2 {
    position: absolute; bottom: -60px; left: 55%;
    width: 220px; height: 220px; border-radius: 50%;
    background: rgba(255,255,255,0.04); pointer-events: none;
}
.hero-watermark {
    position: absolute; bottom: -18px; right: 30px;
    font-size: 100px; font-weight: 800;
    color: rgba(255,255,255,0.04);
    letter-spacing: 4px; pointer-events: none; user-select: none;
}
.hero-tag {
    display: inline-flex; align-items: center; gap: 7px;
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.20);
    color: rgba(255,255,255,0.90);
    font-size: 11px; font-weight: 600; letter-spacing: 1px;
    text-transform: uppercase; padding: 5px 14px; border-radius: 20px; margin-bottom: 18px;
}
.hero-tag::before {
    content: ''; width: 6px; height: 6px;
    border-radius: 50%; background: var(--sky-300);
}
.hero-title {
    font-size: clamp(34px, 4.5vw, 58px); font-weight: 800;
    color: var(--white); line-height: 1.08;
    letter-spacing: -1.5px; margin: 0 0 14px;
}
.hero-title .accent { color: var(--sky-300); }
.hero-desc {
    font-size: 15px; font-weight: 400;
    color: rgba(255,255,255,0.60);
    line-height: 1.75; max-width: 460px; margin-bottom: 30px;
}
.hero-badges { display: flex; gap: 10px; flex-wrap: wrap; }
.hero-badge {
    display: inline-flex; align-items: center; gap: 6px;
    background: rgba(255,255,255,0.10);
    border: 1px solid rgba(255,255,255,0.18);
    color: rgba(255,255,255,0.85);
    font-size: 12px; font-weight: 500; padding: 6px 14px; border-radius: 8px;
}

/* ── SECTION LABEL ── */
.sec-label { display: flex; align-items: center; gap: 10px; margin-bottom: 16px; }
.sec-dot { width: 7px; height: 7px; background: var(--sky-500); border-radius: 50%; }
.sec-text { font-size: 10px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: var(--sky-600); }
.sec-line { flex: 1; height: 1px; background: var(--border); }

/* ── INPUT CARDS ── */
.icard {
    background: var(--white); border: 1px solid var(--border);
    border-radius: 18px; padding: 22px 20px 18px;
    transition: border-color 0.2s, box-shadow 0.2s;
    box-shadow: 0 2px 12px var(--shadow-sm); height: 100%;
}
.icard:hover { border-color: var(--sky-300); box-shadow: 0 6px 28px var(--shadow-md); }
.icard-head {
    display: flex; align-items: center; gap: 11px;
    padding-bottom: 14px; margin-bottom: 16px;
    border-bottom: 1px solid var(--border);
}
.icard-ico {
    width: 38px; height: 38px; border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 18px; flex-shrink: 0;
}
.ico-blue   { background: var(--sky-50); }
.ico-indigo { background: #eef2ff; }
.ico-teal   { background: #f0fdfa; }
.icard-title { font-size: 13px; font-weight: 700; color: var(--text-dark); letter-spacing: -0.1px; }
.icard-sub   { font-size: 11px; color: var(--text-muted); margin-top: 2px; }

/* ── Widget Overrides ── */
.stNumberInput label, .stSelectbox label,
.stRadio > label, .stDateInput label,
.stCheckbox label p {
    font-family: 'Inter', sans-serif !important;
    font-size: 11px !important; font-weight: 600 !important;
    color: var(--text-soft) !important;
    text-transform: uppercase !important; letter-spacing: 0.5px !important;
}
.stNumberInput input, .stDateInput input {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 14px !important; font-weight: 500 !important;
    color: var(--text-dark) !important;
    background: var(--sky-50) !important;
    border: 1.5px solid var(--sky-200) !important;
    border-radius: 10px !important;
}

/* ── RUN BUTTON ── */
div.stButton > button {
    background: var(--sky-600) !important;
    color: white !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 15px !important; font-weight: 700 !important;
    letter-spacing: 1px !important; text-transform: uppercase !important;
    padding: 17px 40px !important; border: none !important;
    border-radius: 14px !important; cursor: pointer !important;
    transition: background 0.15s ease, transform 0.15s ease, box-shadow 0.15s ease !important;
    box-shadow: 0 4px 20px rgba(2,132,199,0.35) !important;
    width: 100% !important;
}
div.stButton > button:hover {
    background: var(--sky-800) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 10px 32px rgba(2,132,199,0.42) !important;
}

/* ── RESULT PANEL ── */
.result-panel {
    background: var(--sky-800);
    border-radius: 22px; padding: 48px 44px 40px; margin-top: 24px;
    position: relative; overflow: hidden;
    border: 1px solid rgba(125,211,252,0.15);
}
.result-label {
    font-size: 11px; font-weight: 600; letter-spacing: 2.5px;
    text-transform: uppercase; color: var(--sky-300);
    text-align: center; margin-bottom: 10px;
}
.result-amount {
    font-family: 'Inter', sans-serif;
    font-size: clamp(40px, 6vw, 72px); font-weight: 800;
    color: var(--white); letter-spacing: -2px;
    text-align: center; line-height: 1.1; margin-bottom: 14px;
}
.result-amount .currency {
    font-size: 0.45em; color: var(--sky-300);
    vertical-align: middle; margin-right: 4px;
}
.result-amount .conversion {
    font-size: 0.35em; color: rgba(125,211,252,0.6);
    display: block; margin-top: 8px; font-weight: 500; letter-spacing: 0;
}
.stat-row { display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; margin-top: 20px; }
.stat-box {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(125,211,252,0.15);
    border-radius: 12px; padding: 12px 22px;
    text-align: center; min-width: 140px;
}
.stat-val { font-family: 'JetBrains Mono', monospace; font-size: 15px; font-weight: 500; color: var(--white); }
.stat-key { font-size: 10px; font-weight: 600; color: rgba(125,211,252,0.55); letter-spacing: 1.2px; text-transform: uppercase; margin-top: 4px; }

/* ── ALERTS ── */
.alert-high { background: #f0fdf4; border-left: 4px solid #16a34a; color: #14532d; border-radius: 12px; padding: 14px 18px; margin-top: 16px; font-size: 14px; font-weight: 500; }
.alert-low { background: #fffbeb; border-left: 4px solid #d97706; color: #78350f; border-radius: 12px; padding: 14px 18px; margin-top: 16px; font-size: 14px; font-weight: 500; }
.alert-normal { background: var(--sky-50); border-left: 4px solid var(--sky-500); color: var(--sky-900); border-radius: 12px; padding: 14px 18px; margin-top: 16px; font-size: 14px; font-weight: 500; }

.footer { text-align: center; margin-top: 48px; padding-top: 20px; border-top: 1px solid var(--border); color: var(--sky-400); font-size: 12px; }
</style>
""", unsafe_allow_html=True)

# ── Indian Number Format Function ──────────────────────────────────────────────
def format_inr(num):
    num = int(num)
    s = str(num)
    if len(s) <= 3: return s
    last3 = s[-3:]
    rest = s[:-3][::-1]
    groups = [rest[i:i+2] for i in range(0, len(rest), 2)]
    return ",".join(groups)[::-1] + "," + last3

# ── Load Model ─────────────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    try:
        with open('models/sales_model.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None

model = load_model()

# ── Navbar ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="navbar">
    <div class="navbar-brand">
        <div class="brand-icon">📊</div>
        <div class="brand-name">Rossmann <span>BI</span></div>
    </div>
    <div class="navbar-right">
        <div class="nav-chip live">● Live</div>
        <div class="nav-chip">ML Engine</div>
        <div class="nav-chip">1115 Stores</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Hero ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-circle-1"></div>
    <div class="hero-circle-2"></div>
    <div class="hero-watermark">ROSSMANN</div>
    <div class="hero-tag">Revenue Intelligence Platform</div>
    <div class="hero-title">Sales Forecast<br><span class="accent">Engine</span></div>
    <div class="hero-desc">Enter parameters to generate ML revenue predictions with INR conversion.</div>
</div>
""", unsafe_allow_html=True)

if model is None:
    st.error("⚠️ Model file not found.")
    st.stop()

# ── Input Section ──────────────────────────────────────────────────────────────
st.markdown('<div class="sec-label"><div class="sec-dot"></div><div class="sec-text">Configure Parameters</div><div class="sec-line"></div></div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown('<div class="icard"><div class="icard-head"><div class="icard-ico ico-blue">🏪</div><div class="icard-title">Store Identity</div></div></div>', unsafe_allow_html=True)
    store_id = st.number_input("Store Number", 1, 1115, 1)
    store_type = st.selectbox("Store Format", [0,1,2,3], format_func=lambda x: ["A Standard","B Flagship","C Medium","D Extended"][x])
    assortment = st.selectbox("Product Mix", [0,1,2], format_func=lambda x: ["Basic","Extra","Extended"][x])

with col2:
    st.markdown('<div class="icard"><div class="icard-head"><div class="icard-ico ico-indigo">📅</div><div class="icard-title">Date & Timing</div></div></div>', unsafe_allow_html=True)
    selected_date = st.date_input("Forecast Date", datetime.now())
    day_of_week = selected_date.isoweekday()
    holiday = st.selectbox("Holiday Period", [0,1,2,3], format_func=lambda x: ["None","Public","Easter","Christmas"][x])

with col3:
    st.markdown('<div class="icard"><div class="icard-head"><div class="icard-ico ico-teal">📈</div><div class="icard-title">Market Factors</div></div></div>', unsafe_allow_html=True)
    promo = st.radio("Active Promotion", [1, 0], format_func=lambda x: "✅ YES" if x==1 else "❌ NO", horizontal=True)
    school_h = st.checkbox("🎒 School Holiday")

# ── Run Button ─────────────────────────────────────────────────────────────────
run = st.button("▶  Run Sales Analytics", use_container_width=True)

# ── Prediction Output ──────────────────────────────────────────────────────────
if run:
    EXCHANGE_RATE = 90.0 # 1 EUR = 90 INR
    
    features = np.array([[store_id, day_of_week, promo, holiday, int(school_h), store_type, assortment]])
    pred_eur = model.predict(features)[0]
    
    pred_inr = pred_eur * EXCHANGE_RATE
    week_inr = (pred_eur * 6) * EXCHANGE_RATE
    month_inr = (pred_eur * 26) * EXCHANGE_RATE

    promo_label = "Active" if promo == 1 else "None"
    holiday_labels = ["None", "Public", "Easter", "Christmas"]

    st.markdown(f"""
    <div class="result-panel">
        <div class="result-label">Predicted Daily Revenue</div>
        <div class="result-amount">
            <span class="currency">₹</span>{format_inr(pred_inr)}
            <span class="conversion">(€{pred_eur:,.2f})</span>
        </div>
        <div class="stat-row">
            <div class="stat-box">
                <div class="stat-val">₹{format_inr(week_inr)}</div>
                <div class="stat-key">Weekly (₹)</div>
            </div>
            <div class="stat-box">
                <div class="stat-val">₹{format_inr(month_inr)}</div>
                <div class="stat-key">Monthly (₹)</div>
            </div>
            <div class="stat-box">
                <div class="stat-val">{promo_label}</div>
                <div class="stat-key">Promo</div>
            </div>
            <div class="stat-box">
                <div class="stat-val">{holiday_labels[holiday]}</div>
                <div class="stat-key">Holiday</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if pred_eur > 8000:
        st.markdown(f'<div class="alert-high">🟢 High Demand: Revenue exceeds ₹{format_inr(8000*EXCHANGE_RATE)}. Increase stock.</div>', unsafe_allow_html=True)
    elif pred_eur < 2000:
        st.markdown(f'<div class="alert-low">🟡 Low Volume: Revenue below ₹{format_inr(2000*EXCHANGE_RATE)}. Add promotions.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="alert-normal">🔵 Normal Day: Revenue is within standard operating range.</div>', unsafe_allow_html=True)

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="footer">Rossmann BI Platform · 1 EUR = ₹90.00 · Internal Use Only</div>', unsafe_allow_html=True)