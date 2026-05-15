# ======================================================
# COFFEELAB PROJECT - OFFICIAL BRAND BRANDING
# Features: Lead Gate, Rarity Weights, Live 24h Clock, HTTP Push DB
# ======================================================

import streamlit as st
import random
import time
from datetime import datetime
import zoneinfo
import requests

# --- CONFIG ---
st.set_page_config(page_title="Coffee Lab Reward Protocol", page_icon="☕", layout="centered")

# 🚨 ΒΑΛΕ ΕΔΩ ΤΟ URL ΠΟΥ ΕΚΑΝΕΣ COPY ΑΠΟ ΤΟ GOOGLE APPS SCRIPT
SCRIPT_URL = "https://box.gr/delivery/ilioupoli/coffee-lab-hlioupolh" 

# --- OFFICIAL COFFEE LAB BRANDING (CSS INJECT) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&family=Share+Tech+Mono&display=swap');
    
    /* Coffee Lab Dark Palette Background */
    .stApp { 
        background: linear-gradient(180deg, #0e0e0e 0%, #171717 100%);
    }
    
    h1, h2, h3, p, span, label {
        font-family: 'Montserrat', sans-serif !important;
        color: #ffffff !important;
    }
    
    /* Coffee Lab Official Yellow/Amber (#ffb800 ή #f3a913) */
    .brand-title {
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 900 !important;
        color: #ffb800 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        text-align: center;
        margin-top: 15px;
        margin-bottom: 5px;
    }
    
    .brand-subtitle {
        text-align: center;
        font-family: 'Share Tech Mono', monospace !important;
        color: #aaaaaa !important;
        font-size: 13px;
        letter-spacing: 2px;
        margin-bottom: 30px;
    }

    /* Input Box styling */
    div['data-baseweb']="input" {
        background-color: #1a1a1a !important;
        border: 1px solid #333333 !important;
        border-radius: 6px !important;
    }
    
    input {
        color: #ffb800 !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: bold !important;
    }

    /* Coffee Lab Premium Yellow Button */
    .stButton>button {
        width: 100%;
        height: 3.8em;
        background-color: #ffb800 !important; 
        color: #000000 !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 900 !important;
        border: none !important;
        border-radius: 6px !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 184, 0, 0.2);
    }
    
    .stButton>button:hover {
        background-color: #ffa800 !important;
        color: #000000 !important;
        box-shadow: 0 0 25px rgba(255, 184, 0, 0.5) !important;
        transform: translateY(-1px);
    }
    
    .stButton>button:disabled {
        background-color: #222222 !important;
        color: #555555 !important;
        border: 1px solid #333333 !important;
        box-shadow: none !important;
        transform: none !important;
    }

    /* Target Acquired Box - Brand Style */
    .success-box {
        background: rgba(255, 184, 0, 0.03);
        border: 2px solid #ffb800;
        border-radius: 8px;
        padding: 25px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 0 20px rgba(255, 184, 0, 0.1);
    }
    
    .success-title {
        color: #ffb800 !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 900 !important;
        font-size: 22px;
        letter-spacing: 1px;
    }
    
    hr {
        border-color: #262626 !important;
    }
    
    /* Center Logo Wrapper */
    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BRAND LOGO INSERT ---
# Χρησιμοποιούμε μια έγκυρη URL εικόνα για το logo. Αν έχεις δικό σου link, αντικαθιστάς το src.
st.markdown("""
    <div class="logo-container">
        <img src="https://coffeelab.gr/wp-content/uploads/2021/10/logo.png" width="160" alt="Coffee Lab Logo">
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
    
    # Brand Styled Success Box
    st.markdown(f"""
        <div class="success-box">
            <div class="success-title">🎯 ΚΕΡΔΙΣΕΣ!</div>
            <p style='font-size: 16px; margin-top: 10px; color: #888888;'>Instagram ID: <span style='color:#ffffff; font-weight:bold;'>{user_name}</span></p>
            <div style='background-color: #111111; padding: 15px; border-radius: 6px; margin-top: 15px; border: 1px solid #222222;'>
                <p style='font-size: 20px; font-weight: 900; color: #ffb800; margin: 0;'>{saved_gift}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.info("ℹ️ Δείξε αυτή την οθόνη ζωντανά στο ταμείο ΚΑΙ παράδωσε τη φυσική κάρτα για να πάρεις το δώρο σου.")
    st.write("---")

    # 🕒 LIVE EMBEDDED CLOCK VIA HTML/JS
    live_clock_html = f"""
    <div id="countdown-box" style="
        font-family: 'Share Tech Mono', monospace;
        font-size: 20px;
        font-weight: bold;
        color: #ff4b4b;
        text-align: center;
        background-color: #141414;
        padding: 15px;
        border-radius: 6px;
        border: 1px solid #222222;
        margin-bottom: 15px;
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
            box.innerHTML = "❌ ΤΟ ΚΟΥΠΟΝΙ ΕΛΗΞΕ!<br><span style='font-size:13px; color:gray;'>🔒 Το χρονικό όριο των 24 ωρών παρήλθε.</span>";
            box.style.borderColor = "#ff4b4b";
        }} else {{
            const hours = Math.floor(remainingTime / 3600);
            const minutes = Math.floor((remainingTime % 3600) / 60);
            const seconds = remainingTime % 60;
            
            const timerStr = 
                (hours < 10 ? "0" : "") + hours + ":" + 
                (minutes < 10 ? "0" : "") + minutes + ":" + 
                (seconds < 10 ? "0" : "") + seconds;
            
            box.innerHTML = "📅 " + dateStr + " — ⏰ " + timeStr + "<br><span style='color:#ffb800;'>⏳ ΛΗΞΗ ΚΟΥΠΟΝΙΟΥ ΣΕ: " + timerStr + "</span>";
        }}
    }}

    setInterval(updateClock, 1000);
    updateClock();
    </script>
    """
    st.components.v1.html(live_clock_html, height=120)
    st.warning("🔒 Η προσπάθεια κλείδωσε για αυτή τη συσκευή. Ισχύει μια εξαργύρωση ανά κάρτα.")

else:
    # 2. INITIAL STATE - DATA CAPTURE (Lead Gate)
    st.markdown("<p style='text-align:center; font-size:15px; font-weight: bold; color: #aaaaaa;'>ΕΙΣΑΓΕΤΕ ΤΑ ΣΤΟΙΧΕΙΑ ΣΑΣ ΓΙΑ ΝΑ ΠΑΙΞΕΤΕ</p>", unsafe_allow_html=True)
    input_name = st.text_input("Όνομα ή Instagram Profile:", value="", placeholder="@username")
    st.write("---")
    
    if input_name.strip() != "":
        st.markdown("<p style='color:#ffb800; text-align:center; font-weight: bold;'>✓ Η ΣΥΝΔΕΣΗ ΕΝΕΡΓΟΠΟΙΗΘΗΚΕ // ΠΑΤΗΣΤΕ ΤΟ ΚΟΥΜΠΙ</p>", unsafe_allow_html=True)
        st.write("")
        
        if st.button('ΔΙΕΚΔΙΚΗΣΗ ΔΩΡΟΥ'):
            with st.spinner('Γίνεται κλήρωση του reward σας...'):
                
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

                # Κλειδώνουμε το URL
                st.query_params["gift"] = final_reward
                st.query_params["t"] = current_ts
                st.query_params["user"] = input_name.strip()
                
                st.rerun()
    else:
        st.button('ΔΙΕΚΔΙΚΗΣΗ ΔΩΡΟΥ (ΠΑΡΑΚΑΛΩ ΕΙΣΑΓΕΤΕ ΟΝΟΜΑ)', disabled=True)
