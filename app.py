import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="XAUUSD AI Trading Assistant", layout="wide")

st.title("🥇 XAUUSD Precision Analyzer & Live Execution Hub")
st.markdown("Designed for FXify $1K Instant Account ($30 Daily Risk / Micro Lots)")
st.markdown("---")

# --- 1. REAL-TIME TRADINGVIEW WIDGET (LIVE DATA) ---
st.subheader("📈 Live Streaming Gold Chart (XAUUSD)")

# Embed TradingView Advanced Chart Widget
tradingview_html = """
<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container" style="height:500px;width:100%;">
  <div id="tradingview_xauusd" style="height:calc(100% - 32px);width:100%;"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget(
  {
  "autosize": true,
  "symbol": "OANDA:XAUUSD",
  "interval": "15",
  "timezone": "Etc/UTC",
  "theme": "dark",
  "style": "1",
  "locale": "en",
  "toolbar_bg": "#f1f3f6",
  "enable_publishing": false,
  "hide_side_toolbar": false,
  "allow_symbol_change": true,
  "container_id": "tradingview_xauusd"
}
  );
  </script>
</div>
<!-- TradingView Widget END -->
"""
components.html(tradingview_html, height=520)

st.markdown("---")

# --- 2. MULTI-ASSET CORRELATION BIAS (LIVE TICKERS) ---
st.subheader("🌐 Related Asset Live Overview (US10Y, DXY, WTI OIL)")

correlation_widgets = """
<!-- TradingView Ticker Tape Widget BEGIN -->
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-tickers.js" async>
  {
  "symbols": [
    {
      "proName": "OANDA:XAUUSD",
      "title": "Gold"
    },
    {
      "proName": "CAPITALCOM:DXY",
      "title": "US Dollar Index"
    },
    {
      "proName": "TVC:US10Y",
      "title": "US 10Y Yield"
    },
    {
      "proName": "TVC:USOIL",
      "title": "Crude Oil"
    }
  ],
  "isTransparent": false,
  "showSymbolLogo": true,
  "colorTheme": "dark",
  "locale": "en"
}
  </script>
</div>
<!-- TradingView Ticker Tape Widget END -->
"""
components.html(correlation_widgets, height=100)

st.markdown("---")

# --- 3. INPUT YOUR TECHNICAL ANALYSIS ---
st.subheader("🔍 Enter Your Chart Observations")

col_ta1, col_ta2 = st.columns(2)

with col_ta1:
    structure = st.selectbox("Market Structure (15M / 1H):", ["Select...", "Bullish Break of Structure (BOS)", "Bearish Break of Structure (BOS)", "Consolidating / Ranging"])
    zone = st.selectbox("Key Zone Interaction:", ["Select...", "At Demand / Support Zone", "At Supply / Resistance Zone", "In No-Man's Land"])

with col_ta2:
    candle_pattern = st.selectbox("Price Action Confirmation:", ["Select...", "Bullish Engulfing / Reversal Pinbar", "Bearish Engulfing / Reversal Pinbar", "No Clear Pattern"])
    dxy_correlation = st.selectbox("DXY (Dollar) & Yields Direction:", ["Select...", "DXY Dumping / Weak Yields", "DXY Pumping / Strong Yields", "DXY Neutral"])

# --- 4. PREDICTION ENGINE ---
st.markdown("---")
st.subheader("🤖 AI Correlation & Trade Evaluator")

if st.button("Analyze Confluence & Generate Prediction", use_container_width=True):
    # Calculation Logic
    bullish_signals = 0
    bearish_signals = 0
    
    if structure == "Bullish Break of Structure (BOS)": bullish_signals += 1
    elif structure == "Bearish Break of Structure (BOS)": bearish_signals += 1
        
    if zone == "At Demand / Support Zone": bullish_signals += 1
    elif zone == "At Supply / Resistance Zone": bearish_signals += 1
        
    if candle_pattern == "Bullish Engulfing / Reversal Pinbar": bullish_signals += 1
    elif candle_pattern == "Bearish Engulfing / Reversal Pinbar": bearish_signals += 1
        
    if dxy_correlation == "DXY Dumping / Weak Yields": bullish_signals += 1
    elif dxy_correlation == "DXY Pumping / Strong Yields": bearish_signals += 1

    st.markdown("### 📊 Trade Prediction Output:")

    if bullish_signals >= 3 and bearish_signals == 0:
        st.success("🟢 **HIGH PROBABILITY BUY (BID) PREDICTION**")
        st.write("**Execution Guidelines:**")
        st.write("- Asset: XAUUSD (Gold)")
        st.write("- Action: BUY / BID")
        st.write("- Recommended Volume: **0.01 Micro Lot**")
        st.write("- Stop Loss: Set 20–30 pips below the demand zone swing low ($2.00–$3.00 risk).")
        
    elif bearish_signals >= 3 and bullish_signals == 0:
        st.error("🔴 **HIGH PROBABILITY SELL (ASK) PREDICTION**")
        st.write("**Execution Guidelines:**")
        st.write("- Asset: XAUUSD (Gold)")
        st.write("- Action: SELL / ASK")
        st.write("- Recommended Volume: **0.01 Micro Lot**")
        st.write("- Stop Loss: Set 20–30 pips above the supply zone swing high ($2.00–$3.00 risk).")
        
    elif bullish_signals > 0 and bearish_signals > 0:
        st.warning("⚠️ **CONFLICTING SIGNALS / MIXED BIAS**")
        st.write("Market structure and correlated assets (DXY/Yields) are contradicting each other.")
        st.write("**Recommendation:** STAND ASIDE. Protect your $30 daily loss limit!")
        
    else:
        st.info("ℹ️ **NO HIGH-PROBABILITY SETUP**")
        st.write("Insufficient confluence to justify placing a order. Wait for price to reach a key zone.")

# --- 5. FXIFY RISK CALCULATOR ---
st.markdown("---")
st.subheader("🛡️ FXify Account Risk Guard")
sl_pips = st.number_input("Enter Stop Loss distance in Pips/Points:", min_value=5, max_value=100, value=25)
risk_amount = (sl_pips * 0.10) # 0.01 Lot on Gold = $0.10 per pip
st.write(f"Estimated Loss if SL is hit (0.01 Lot): **${risk_amount:.2f}**")

if risk_amount > 3.00:
    st.error("❌ Warning: Risk exceeds $3.00 per trade limit for a $1,000 account!")
else:
    st.success("✅ Risk is within safe operating parameters.")
    
