# ======================================================
# COFFEELAB PROJECT - HIGH-END CYBERPUNK UI
# Features: Lead Gate, Rarity Weights, Live 24h Clock, HTTP Push DB
# ======================================================

import streamlit as st
import random
import time
from datetime import datetime
import zoneinfo
import requests

# --- CONFIG ---
st.set_page_config(page_title="CoffeeLab x Aris", page_icon="☕", layout="centered")

# 🚨 ΒΑΛΕ ΕΔΩ ΤΟ URL ΠΟΥ ΕΚΑΝΕΣ COPY ΑΠΟ ΤΟ GOOGLE APPS SCRIPT
SCRIPT_URL = "ΕΔΩ_ΒΑΛΕ_ΤΟ_URL_ΣΟΥ" 

# --- PREMIUM CYBERPUNK UI CODE (CSS INJECT) ---
st.markdown("""
    <style>
    /* Main Background & Font Upgrade */
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@500;700&display=swap');
    
    .stApp { 
        background: linear-gradient(135deg, #020202 0%, #080d05 100%);
    }
    
    h1, h2, h3, p, span, label {
        font-family: 'Share Tech Mono', monospace !important;
        color: #ffffff !important;
    }
    
    /* Neon Title Upgrade */
    .cyber-title {
        font-family: 'Orbitron', sans-serif !important;
        color: #00ff41 !important;
        text-shadow: 0 0 10px rgba(0, 255, 65, 0.6);
        text-transform: uppercase;
        letter-spacing: 2px;
        text-align: center;
        margin-bottom: 5px;
    }
    
    .cyber-subtitle {
        text-align: center;
        color: #888888 !important;
        font-size: 14px;
        letter-spacing: 1px;
        margin-bottom: 30px;
    }

    /* Custom Input Box styling */
    div['data-baseweb']="input" {
        background-color: #111111 !important;
        border: 1px solid #333333 !important;
        border-radius: 4px !important;
    }
    
    input {
        color: #00ff41 !important;
        font-family: 'Share Tech Mono', monospace !important;
    }

    /* Premium Button Override with Hover Glow */
    .stButton>button {
        width: 100%;
        height: 3.8em;
        background-color: #00ff41 !important; 
        color: #000000 !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 4px !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 4px 15px rgba(0, 255, 65, 0.2);
    }
    
    .stButton>button:hover {
        background-color: #00ff41 !important;
        color: #000000 !important;
        box-shadow: 0 0 25px rgba(0, 255, 65, 0.7) !important;
        transform: translateY(-2px);
    }
    
    .stButton>button:disabled {
        background-color: #111111 !important;
        color: #444444 !important;
        border: 1px solid #222222 !important;
        box-shadow: none !important;
        transform: none !important;
    }

    /* Target Acquired Box */
    .success-box {
        background: rgba(0, 255, 65, 0.05);
        border: 1px solid #00ff41;
        border-radius: 6px;
        padding: 20px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: inset 0 0 10px rgba(0, 255, 65, 0.1);
    }
    
    .success-title {
        color: #00ff41 !important;
        font-family: 'Orbitron', sans-serif !important;
        font-size: 20px;
        font-weight: bold;
    }
    
    hr {
        border-color: #112211 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADERS ---
st.markdown('<h1 class="cyber-title">⚡ SYSTEM ACCESS</h1>', unsafe_allow_html=True)
st.markdown('<p class="cyber-subtitle">COFFEELAB x ARIS // PROTOCOL INITIALIZATION</p>', unsafe_allow_html=True)

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
    
    # Custom Styled Box αντί για το κλασικό st.success
    st.markdown(f"""
        <div class="success-box">
            <div class="success-title">🎯 REWARD SECURED</div>
            <p style='font-size: 18px; margin-top: 10px;'>Agent: <span style='color:#00ff41;'>{user_name}</span></p>
            <p style='font-size: 22px; font-weight: bold; color: #00ff41;'>{saved_gift}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.info("ℹ️ Δείξε αυτή την οθόνη ζωντανά στο ταμείο ΚΑΙ παράδωσε τη φυσική κάρτα για την εξαργύρωση.")
    st.write("---")

    # 🕒 LIVE EMBEDDED CLOCK VIA HTML/JS
    live_clock_html = f"""
    <div id="countdown-box" style="
        font-family: 'Share Tech Mono', monospace;
        font-size: 22px;
        font-weight: bold;
        color: #ff4b4b;
        text-align: center;
        background-color: #0b0202;
        padding: 15px;
        border-radius: 4px;
        border: 1px solid #ff4b4b;
        margin-bottom: 15px;
        box-shadow: 0 0 10px rgba(255, 75, 75, 0.1);
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
            box.innerHTML = "❌ ΤΟ ΚΟΥΠΟΝΙ ΕΛΗΞΕ!<br><span style='font-size:14px; color:gray;'>🔒 Το χρονικό όριο των 24 ωρών παρήλθε.</span>";
            box.style.borderColor = "gray";
            box.style.color = "#ff4b4b";
        }} else {{
            const hours = Math.floor(remainingTime / 3600);
            const minutes = Math.floor((remainingTime % 3600) / 60);
            const seconds = remainingTime % 60;
            
            const timerStr = 
                (hours < 10 ? "0" : "") + hours + ":" + 
                (minutes < 10 ? "0" : "") + minutes + ":" + 
                (seconds < 10 ? "0" : "") + seconds;
            
            box.innerHTML = "📅 " + dateStr + " — ⏰ " + timeStr + "<br><span style='color:#00ff41;'>⏳ SECURE LINK EXPIRES IN: " + timerStr + "</span>";
        }}
    }}

    setInterval(updateClock, 1000);
    updateClock();
    </script>
    """
    st.components.v1.html(live_clock_html, height=120)
    st.warning("🔒 Το σύστημα κλείδωσε. Δεν επιτρέπονται επιπλέον προσπάθειες από αυτή τη συσκευή.")

else:
    # 2. INITIAL STATE - DATA CAPTURE (Lead Gate)
    st.markdown("<p style='text-align:center; font-size:16px;'>🔒 USER VERIFICATION REQUIRED</p>", unsafe_allow_html=True)
    input_name = st.text_input("Εισάγετε Όνομα ή Instagram Profile:", value="", placeholder="@username")
    st.write("---")
    
    if input_name.strip() != "":
        st.markdown("<p style='color:#00ff41; text-align:center;'>✅ CONNECTION SECURE // READY TO GENERATE</p>", unsafe_allow_html=True)
        st.write("")
        
        if st.button('INITIALIZE REWARD HACK'):
            with st.spinner('Injecting Data Package...'):
                
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
        st.button('GENERATE REWARD (ENTER ID FIRST)', disabled=True)
