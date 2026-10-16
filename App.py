import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Gold AI Analyzer", layout="centered")

st.markdown("# 🥇 XAUUSD Precision Analyzer")
st.markdown("### Mobile Terminal for FXify $1K Account")
st.markdown("---")

# Fetch Live Data
@st.cache_data(ttl=60)
def get_market_data():
    try:
        gold = yf.download("GC=F", period="2d", interval="1h", progress=False)['Close'].iloc[-1]
        dxy = yf.download("DX-Y.NYB", period="2d", interval="1h", progress=False)['Close'].iloc[-1]
        yields = yf.download("^TNX", period="2d", interval="1h", progress=False)['Close'].iloc[-1]
        return float(gold), float(dxy), float(yields)
    except:
        return 2650.0, 104.5, 4.2 # Fallback baseline

gold_price, dxy_val, yield_val = get_market_data()

# Display Metrics neatly on Mobile
st.metric("Live Gold (GC=F)", f"${gold_price:.2f}")
c1, c2 = st.columns(2)
c1.metric("DXY Index", f"{dxy_val:.2f}")
c2.metric("US 10Y Yield", f"{yield_val:.2f}%")

st.markdown("---")
st.markdown("### 🧠 AI Confirmation Checklist")
st.write("Check all boxes that align before opening MT5:")

trend_up = st.checkbox("1. 1H Market Structure matches my direction")
zone_hit = st.checkbox("2. Price is touching a major 4H/Daily Support or Resistance")
dxy_align = st.checkbox("3. DXY / Yields are moving inversely to the trade")
no_news = st.checkbox("4. No high-impact US news in the next 30 minutes")

if st.button("🚀 Evaluate Entry Probability", use_container_width=True):
    score = sum([trend_up, zone_hit, dxy_align, no_news])
    
    st.markdown("### 📊 Decision Result:")
    if score == 4:
        st.success("✅ **HIGH CONFIRMATION (4/4)**\n- Setup meets criteria.\n- **Lot Size Limit:** Strictly 0.01 Lot ($3 risk max).")
    elif score >= 2:
        st.warning("⚠️ **MODERATE SETUP**\n- Partial confluence. Risk is high, proceed with extreme caution.")
    else:
        st.error("❌ **NO TRADE / STAND ASIDE**\n- Low confirmation. Protect your $30 daily limit!")

st.markdown("---")
st.markdown("### 🛡️ $1K Account Safety Rules")
st.info("""
- **Max Daily Loss:** $30.00 hard limit.
- **Per-Trade Risk:** $3.00 (Max 30 pips SL on 0.01 lot).
- **Rule:** If you take 2 losses in a row, close MT5 for the day.
""")
