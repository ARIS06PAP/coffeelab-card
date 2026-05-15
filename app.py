# ======================================================
# COFFEELAB PROJECT - THE DEFINITIVE MOBILE ENGINE (100% CENTERED)
# Features: Global CSS Reset, Force Center Layout, Lead Gate, Rarity Weights
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

# --- THE ULTIMATE GLOBAL MOBILE RESET & CENTER (CSS INJECT) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&family=Share+Tech+Mono&display=swap');
    
    /* 1. Global Reset & Streamlit Native Element Override */
    [data-testid="stHeader"], footer {
        display: none !important;
    }
    
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 1.5rem !important;
        padding-left: 1.2rem !important;
        padding-right: 1.2rem !important;
        max-width: 450px !important; /* Ιδανικό πλάτος για να "σφίξει" σε mobile view */
        margin: 0 auto !important;
    }
    
    /* Coffee Lab Official Cyan Background */
    .stApp { 
        background: linear-gradient(180deg, #00b4d8 0%, #0077b6 100%);
    }
    
    /* 2. FORCE ABSOLUTE CENTER ON EVERYTHING */
    .element-container, .stVerticalBlock, [data-testid="stVerticalBlock"] {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        width: 100% !important;
        text-align: center !important;
    }
    
    /* Εξουδετέρωση του αριστερού alignment της εικόνας από το Streamlit */
    [data-testid="stImage"], [data-testid="stImage"] img {
        display: block !important;
        margin-left: auto !important;
        margin-right: auto !important;
        text-align: center !important;
        width: 140px !important; /* Ελαφρώς μεγαλύτερο και καθαρό */
    }
    
    /* 3. TYPOGRAPHY & SCALING UPTICK (Λίγο πιο μεγάλα και bold) */
    h1, h2, h3, p, span, label {
        font-family: 'Montserrat', sans-serif !important;
        color: #ffffff !important;
        text-align: center !important;
    }
    
    .brand-title {
        font-family: 'Impact', 'Montserrat', sans-serif !important;
        font-weight: 900 !important;
        color: #ffffff !important;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-top: 10px !important;
        margin-bottom: 4px !important;
        font-size: 28px !important; /* Μεγαλύτερος, καθαρός τίτλος */
        text-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
        width: 100% !important;
    }
    
    .brand-subtitle {
        font-family: 'Share Tech Mono', monospace !important;
        color: #f1f1f1 !important;
        font-size: 12px !important; /* Πιο ευανάγνωστο */
        letter-spacing: 1.5px;
        margin-bottom: 20px !important;
        text-shadow: 0 1px 4px rgba(0, 0, 0, 0.2);
        width: 100% !important;
    }

    /* 4. PERFECT MOBILE INPUT BOX */
    div['data-baseweb']="input" {
        background-color: rgba(15, 15, 15, 0.92) !important;
        border: 2px solid #ffffff !important;
        border-radius: 8px !important;
        height: 52px !important; /* Άνετο μέγεθος */
        width: 100% !important;
    }
    
    input {
        color: #00b4d8 !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: bold !important;
        font-size: 16px !important; /* Κλειδώνει το Zoom στα iPhone */
        text-align: center !important; /* Κεντράρει και το κείμενο που γράφει ο χρήστης */
    }
    
    .stTextInput {
        width: 100% !important;
    }
    
    .stTextInput label p {
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 14px !important;
        margin-bottom: 6px !important;
        text-align: center !important;
        width: 100% !important;
    }

    /* 5. THUMB-FRIENDLY ACTION BUTTON */
    .stButton {
        width: 100% !important;
    }
    
    .stButton>button {
        width: 100% !important;
        height: 54px !important; /* Premium ύψος για εύκολο tap */
        background-color: #0f0f0f !important; 
        color: #ffffff !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 900 !important;
        border: 2px solid #ffffff !important;
        border-radius: 8px !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 16px !important; /* Πιο έντονα γράμματα */
        transition: all 0.2s ease;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
    }
    
    .stButton>button:active {
        background-color: #ffffff !important;
        color: #0077b6 !important;
        transform: scale(0.98);
    }
    
    .stButton>button:disabled {
        background-color: rgba(15, 15, 15, 0.5) !important;
        color: #777777 !important;
        border: 2px solid rgba(255, 255, 255, 0.2) !important;
    }

    /* 6. SUCCESS COUPON SCREEN BLOCK */
    .success-box {
        background: rgba(15, 15, 15, 0.92);
        border: 2px solid #ffffff;
        border-radius: 8px;
        padding: 20px;
        text-align: center;
        width: 100% !important;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
    }
    
    .success-title {
        color: #00b4d8 !important;
        font-family: 'Impact', sans-serif !important;
        font-size: 26px;
        letter-spacing: 1px;
    }
    
    .stAlert {
        padding: 10px !important;
        font-size: 13px !important;
        width: 100% !important;
    }
    
    hr {
        border-color: rgba(255, 255, 255, 0.25) !important;
        width: 100% !important;
        margin-top: 12px !important;
        margin-bottom: 12px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOCAL LOGO LOAD ---
try:
    image = Image.open('logolab.png')
    st.image(image)
except:
    st.markdown("""
        <div style="display:flex; justify-content:center; align-items:center; flex-direction: column; margin-top:5px; margin-bottom:5px;">
            <span style="font-family: 'Impact', sans-serif; font-size: 36px; font-weight: 900; color: #ffffff; line-height: 0.9;">COFFEE</span>
            <span style="font-family: 'Impact', sans-serif; font-size: 36px; font-weight: 900; color: #0f0f0f; letter-spacing: 2px;">LAB</span>
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
            <p style='font-size: 15px; margin-top: 4px; color: #aaaaaa; margin-bottom: 0;'>Instagram ID: <span style='color:#ffffff; font-weight:bold;'>{user_name}</span></p>
            <div style='background-color: #0077b6; padding: 12px; border-radius: 6px; margin-top: 10px; border: 1px solid #ffffff;'>
                <p style='font-size: 18px; font-weight: 900; color: #ffffff; margin: 0;'>{saved_gift}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.info("ℹ️ Δείξε την οθόνη στο ταμείο και παράδωσε τη φυσική κάρτα.")
    st.write("---")

    # 🕒 LIVE EMBEDDED CLOCK VIA HTML/JS
    live_clock_html = f"""
    <div id="countdown-box" style="
        font-family: 'Share Tech Mono', monospace;
        font-size: 16px;
        font-weight: bold;
        color: #ff4b4b;
        text-align: center;
        background-color: #0f0f0f;
        padding: 12px;
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
    st.markdown("<p style='text-align:center; font-size:14px; font-weight: bold; color: #ffffff; text-shadow: 0 1px 3px rgba(0,0,0,0.3); margin-bottom:4px;'>ΕΙΣΑΓΕΤΕ ΤΑ ΣΤΟΙΧΕΙΑ ΣΑΣ ΓΙΑ ΝΑ ΠΑΙΞΕΤΕ</p>", unsafe_allow_html=True)
    input_name = st.text_input("Όνομα ή Instagram Profile:", value="", placeholder="@username")
    st.write("---")
    
    if input_name.strip() != "":
        st.markdown("<p style='color:#ffffff; text-align:center; font-weight: bold; font-size:14px; text-shadow: 0 1px 3px rgba(0,0,0,0.3); margin-bottom:4px;'>✓ Η ΣΥΝΔΕΣΗ ΕΝΕΡΓΟΠΟΙΗΘΗΚΕ</p>", unsafe_allow_html=True)
        
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
