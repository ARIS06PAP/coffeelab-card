# ======================================================
# COFFEELAB PROJECT - MAXIMUM MOBILE OPTIMIZED
# Features: Viewport Lock, No-Scroll UI, Lead Gate, Rarity Weights, Live 24h Clock
# ======================================================

import streamlit as st
import random
import time
from datetime import datetime
import zoneinfo
import requests
from PIL import Image

# --- CONFIG ---
st.set_page_config(page_title="Coffee Lab Rewards", page_icon="☕", layout="centered")

# 🚨 PRODUCTION GOOGLE APPS SCRIPT URL LOCKED
SCRIPT_URL = "https://script.google.com/macros/s/AKfycbw2qkoK1xDY9uZnRWXso3yjAbK-iV5KOW2IcSyaEPrQlEItfWkPZjQr_elQA2Fz3ZDNwg/exec"

# --- 100% MOBILE SCREEN OPTIMIZATION (CSS INJECT) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&family=Share+Tech+Mono&display=swap');
    
    /* Mobile Viewport Reset - Σφίξιμο όλου του container */
    .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 0.5rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 100% !important;
    }
    
    /* Εξαφανίζει τα default Streamlit headers/footers για να κερδίσουμε ύψος */
    [data-testid="stHeader"], footer {
        display: none !important;
    }
    
    /* Coffee Lab Official Cyan Gradient */
    .stApp { 
        background: linear-gradient(180deg, #00b4d8 0%, #0077b6 100%);
        overflow: hidden !important; /* Απαγορεύει το περίεργο scroll στο κινητό */
    }
    
    h1, h2, h3, p, span, label {
        font-family: 'Montserrat', sans-serif !important;
        color: #ffffff !important;
    }
    
    /* Mobile-Perfect Logo Sizing */
    .mobile-logo-wrapper {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 5px;
        margin-bottom: 5px;
    }
    .mobile-logo-wrapper img {
        max-height: 75px !important; /* Κλειδωμένο ύψος για να μην σπρώχνει την οθόνη */
        width: auto !important;
    }
    
    /* Mobile Optimized Titles */
    .brand-title {
        font-family: 'Impact', 'Montserrat', sans-serif !important;
        font-weight: 900 !important;
        color: #ffffff !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        text-align: center;
        margin-top: 0px;
        margin-bottom: 2px;
        font-size: 24px !important; /* Ιδανικό για iPhone/Android screens */
        text-shadow: 0 2px 6px rgba(0, 0, 0, 0.25);
    }
    
    .brand-subtitle {
        text-align: center;
        font-family: 'Share Tech Mono', monospace !important;
        color: #f1f1f1 !important;
        font-size: 10px !important;
        letter-spacing: 1px;
        margin-bottom: 12px;
        text-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
    }

    /* Mobile Friendly Input Box */
    div['data-baseweb']="input" {
        background-color: rgba(15, 15, 15, 0.9) !important;
        border: 2px solid #ffffff !important;
        border-radius: 8px !important;
        height: 48px !important; /* Ιδανικό ύψος για mobile tapping */
    }
    
    input {
        color: #00b4d8 !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: bold !important;
        font-size: 16px !important; /* Αποτρέπει το αυτόματο Zoom-in στα iPhone */
    }
    
    .stTextInput label p {
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 12px !important;
        margin-bottom: 4px !important;
    }

    /* Thumb-Friendly Big Button */
    .stButton>button {
        width: 100%;
        height: 52px !important; /* Μεγάλο target area για τον αντίχειρα */
        background-color: #0f0f0f !important; 
        color: #ffffff !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 900 !important;
        border: 2px solid #ffffff !important;
        border-radius: 8px !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 15px !important;
        transition: all 0.2s ease;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
        margin-top: 5px;
    }
    
    .stButton>button:active {
        background-color: #ffffff !important;
        color: #0077b6 !important;
        transform: scale(0.98);
    }
    
    .stButton>button:disabled {
        background-color: rgba(15, 15, 15, 0.4) !important;
        color: #777777 !important;
        border: 2px solid rgba(255, 255, 255, 0.2) !important;
    }

    /* Mobile Compact Success Card */
    .success-box {
        background: rgba(15, 15, 15, 0.9);
        border: 2px solid #ffffff;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
        margin-bottom: 12px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
    }
    
    .success-title {
        color: #00b4d8 !important;
        font-family: 'Impact', sans-serif !important;
        font-size: 22px;
        letter-spacing: 1px;
    }
    
    /* Μάζεμα των default κενών των ειδοποιήσεων */
    .stAlert {
        padding: 8px !important;
        font-size: 12px !important;
    }
    
    hr {
        border-color: rgba(255, 255, 255, 0.25) !important;
        margin-top: 8px !important;
        margin-bottom: 8px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOCAL LOGO LOAD (MOBILE OPTIMIZED WRAPPER) ---
try:
    image = Image.open('logolab.png')
    st.markdown('<div class="mobile-logo-wrapper">', unsafe_allow_html=True)
    st.image(image, width=120) # Ελεγχόμενο πλάτος
    st.markdown('</div>', unsafe_allow_html=True)
except:
    st.markdown("""
        <div style="display:flex; justify-content:center; align-items:center; flex-direction: column; margin-top:5px; margin-bottom:5px;">
            <span style="font-family: 'Impact', sans-serif; font-size: 32px; font-weight: 900; color: #ffffff; line-height: 0.9;">COFFEE</span>
            <span style="font-family: 'Impact', sans-serif; font-size: 32px; font-weight: 900; color: #0f0f0f; letter-spacing: 2px;">LAB</span>
        </div>
    """, unsafe_allow_html=True)

# --- HEADERS ---
st.markdown('<h1 class="brand-title">LUCKY REWARD PROTOCOL</h1>', unsafe_allow_html=True)
st.markdown('<p class="brand-subtitle">SCAN & WIN // OFFICIAL COFFEE LAB HANDOUT</p>', unsafe_allow_html=True)

rewards = [
    "🎁 1+1 Καφές (Optimization Protocol)",
    "🎁 -20% στην επόμενη παραγγελία",
    "🎁 Δωρεάν Snack / Cookie",
    "🎁 Upgrade σε Large μέγεθος",
    "🎁 Free Extra Shot (Energy Boost)"
]
reward_weights = [5, 15, 15, 32.5, 32.5]

query_params = st.query_params

# 1. CHECK STATUS (Αν ο χρήστης έχει ήδη κλειδωμένο δώρο)
if "gift" in query_params:
    saved_gift = query_params["gift"]
    user_name = query_params.get("user", "Agent")
    start_ts = query_params["t"]

    st.balloons()
    
    st.markdown(f"""
        <div class="success-box">
            <div class="success-title">🎯 ΚΕΡΔΙΣΕΣ!</div>
            <p style='font-size: 14px; margin-top: 3px; color: #aaaaaa; margin-bottom: 0;'>Instagram ID: <span style='color:#ffffff; font-weight:bold;'>{user_name}</span></p>
            <div style='background-color: #0077b6; padding: 10px; border-radius: 6px; margin-top: 8px; border: 1px solid #ffffff;'>
                <p style='font-size: 16px; font-weight: 900; color: #ffffff; margin: 0;'>{saved_gift}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.info("ℹ️ Δείξε την οθόνη στο ταμείο και παράδωσε τη φυσική κάρτα.")
    st.write("---")

    # 🕒 LIVE EMBEDDED CLOCK VIA HTML/JS (COMPACT)
    live_clock_html = f"""
    <div id="countdown-box" style="
        font-family: 'Share Tech Mono', monospace;
        font-size: 16px;
        font-weight: bold;
        color: #ff4b4b;
        text-align: center;
        background-color: #0f0f0f;
        padding: 10px;
        border-radius: 8px;
        border: 2px solid #ff4b4b;
    ">
        Initializing Real-Time Clock...
    </div>

    <script>
    const startTimestamp = parseInt("{start_ts}");
    
    function updateClock() {{
        const now = new Date();
        const currentTimestamp = Math.floor(Date.now() / 1000);
        
        const timeStr = now.toLocaleTimeString('el-GR', {{ hour12: false }});
        const dateStr = now.toLocaleDateString('el-GR');
        
        const elapsedTime = currentTimestamp - startTimestamp;
        const remainingTime = 86400 - elapsedTime;
        
        const box = document.getElementById("countdown-box");
        
        if (remainingTime <= 0) {{
            box.innerHTML = "❌ ΤΟ ΚΟΥΠΟΝΙ ΕΛΗΞΕ!<br><span style='font-size:11px; color:gray;'>🔒 Το χρονικό όριο των 24 ωρών παρήλθε.</span>";
            box.style.borderColor = "#ff4b4b";
        }} else {{
            const hours = Math.floor(remainingTime / 3600);
            const minutes = Math.floor((remainingTime % 3600) / 60);
            const seconds = remainingTime % 60;
            
            const timerStr = 
                (hours < 10 ? "0" : "") + hours + ":" + 
                (minutes < 10 ? "0" : "") + minutes + ":" + 
                (seconds < 10 ? "0" : "") + seconds;
            
            box.innerHTML = "📅 " + dateStr + " — ⏰ " + timeStr + "<br><span style='color:#00b4d8;'>⏳ ΛΗΞΗ ΣΕ: " + timerStr + "</span>";
        }}
    }}

    setInterval(updateClock, 1000);
    updateClock();
    </script>
    """
    st.components.v1.html(live_clock_html, height=90)
    st.warning("🔒 Η προσπάθεια κλείδωσε. Ισχύει μια εξαργύρωση ανά κάρτα.")

else:
    # 2. INITIAL STATE - DATA CAPTURE (Lead Gate)
    st.markdown("<p style='text-align:center; font-size:13px; font-weight: bold; color: #ffffff; text-shadow: 0 1px 3px rgba(0,0,0,0.3); margin-bottom:2px;'>ΕΙΣΑΓΕΤΕ ΤΑ ΣΤΟΙΧΕΙΑ ΣΑΣ ΓΙΑ ΝΑ ΠΑΙΞΕΤΕ</p>", unsafe_allow_html=True)
    input_name = st.text_input("Όνομα ή Instagram Profile:", value="", placeholder="@username")
    st.write("---")
    
    if input_name.strip() != "":
        st.markdown("<p style='color:#ffffff; text-align:center; font-weight: bold; font-size:13px; text-shadow: 0 1px 3px rgba(0,0,0,0.3); margin-bottom:2px;'>✓ Η ΣΥΝΔΕΣΗ ΕΝΕΡΓΟΠΟΙΗΘΗΚΕ</p>", unsafe_allow_html=True)
        
        if st.button('ΔΙΕΚΔΙΚΗΣΗ ΔΩΡΟΥ'):
            with st.spinner('Κλήρωση...'):
                
                final_reward = random.choices(rewards, weights=reward_weights, k=1)[0]
                current_ts = str(int(time.time()))
                
                # 📊 BACKGROUND GOOGLE PUSH (HTTP POST)
                tz = zoneinfo.ZoneInfo("Europe/Athens")
                now_gr = datetime.now(tz)
                
                payload = {
                    "Date": now_gr.strftime("%d/%m/%Y"),
                    "Time": now_gr.strftime("%H:%M:%S"),
                    "User": input_name.strip(),
                    "Reward": final_reward
                }
                
                try:
                    requests.post(SCRIPT_URL, json=payload, timeout=5)
                except:
                    pass 

                st.query_params["gift"] = final_reward
                st.query_params["t"] = current_ts
                st.query_params["user"] = input_name.strip()
                
                st.rerun()
    else:
        st.button('ΔΙΕΚΔΙΚΗΣΗ ΔΩΡΟΥ (ΕΙΣΑΓΕΤΕ ΟΝΟΜΑ)', disabled=True)
