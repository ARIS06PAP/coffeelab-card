# ======================================================
# COFFEELAB PROJECT - ENTERPRISE EDITION
# Features: Lead Capture, Rarity Weights, Anti-Cheat URL, Live Clock
# ======================================================

import streamlit as st
import random
import time

# --- CONFIG ---
st.set_page_config(page_title="CoffeeLab x Aris", page_icon="☕")

# Clean & Dark Look
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    .stButton>button {
        width: 100%;
        height: 3.5em;
        background-color: #00ff41; 
        color: black;
        font-weight: bold;
        border: none;
        text-transform: uppercase;
    }
    .stSuccess { background-color: #1e1e1e; color: #00ff41; border: 1px solid #00ff41; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ System Access Granted")
st.subheader("CoffeeLab x Aris Project")
st.write("---")

# 1. LIST OF REWARDS & WEIGHTS (Rarity Protocol)
rewards = [
    "🎁 1+1 Καφές (Optimization Protocol)", # Legendary
    "🎁 -20% στην επόμενη παραγγελία",         # Rare
    "🎁 Δωρεάν Snack / Cookie",              # Rare
    "🎁 Upgrade σε Large μέγεθος",            # Common
    "🎁 Free Extra Shot (Energy Boost)"       # Common
]

# Πιθανότητες για κάθε δώρο αντίστοιχα (Σύνολο = 100)
# 5% για το 1+1, 15% για το καθένα από τα μεσαία, 32.5% για τα μικρά
reward_weights = [5, 15, 15, 32.5, 32.5]

# Διαβάζουμε τα Query Params από το URL
query_params = st.query_params

# 2. CHECK STATUS (Αν ο χρήστης έχει ήδη παίξει)
if "gift" in query_params:
    saved_gift = query_params["gift"]
    user_name = query_params.get("user", "Agent") # Παίρνει το όνομα από το URL
    start_ts = query_params["t"]

    st.balloons()
    # Εξατομικευμένο μήνυμα επιτυχίας με το όνομα του πελάτη
    st.success(f"TARGET ACQUIRED: {user_name} -> {saved_gift}")
    st.write("---")
    st.info("Δείξε αυτή την οθόνη ζωντανά στον Δημήτρη ή στο ταμείο για το redeem.")

    # 🕒 LIVE EMBEDDED CLOCK VIA HTML/JS
    live_clock_html = f"""
    <div id="countdown-box" style="
        font-family: monospace;
        font-size: 22px;
        font-weight: bold;
        color: #ff4b4b;
        text-align: center;
        background-color: #1a1a1a;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #ff4b4b;
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
            
            box.innerHTML = "📅 " + dateStr + " — ⏰ " + timeStr + "<br><span style='color:#00ff41;'>⏳ ΛΗΞΗ ΣΕ: " + timerStr + "</span>";
        }}
    }}

    setInterval(updateClock, 1000);
    updateClock();
    </script>
    """
    st.components.v1.html(live_clock_html, height=120)
    st.warning("🔒 Το σύστημα κλείδωσε. Δεν επιτρέπονται επιπλέον προσπάθειες.")

else:
    # 3. INITIAL STATE - DATA CAPTURE
    st.markdown("**User Verification Required.**")
    
    # Input πεδίο για το όνομα/Instagram
    input_name = st.text_input("Πληκτρολόγησε το Όνομα ή το Instagram σου για να ξεκλειδώσεις το reward:", "" )
    
    st.write("---")
    
    # Το κουμπί ενεργοποιείται ΜΟΝΟ αν ο χρήστης έχει γράψει τουλάχιστον 2 χαρακτήρες
    if input_name.strip() != "":
        st.markdown("✅ *Στοιχεία έγκυρα. Το σύστημα είναι έτοιμο.*")
        
        if st.button('GENERATE REWARD'):
            with st.spinner('Accessing Database...'):
                time.sleep(0.8)
                
                # Χρήση random.choices με weights για το Rarity Protocol
                # Το [0] χρειάζεται γιατί η choices επιστρέφει λίστα
                final_reward = random.choices(rewards, weights=reward_weights, k=1)[0]
                current_ts = str(int(time.time()))
                
                # Κλειδώνουμε το δώρο, το timestamp ΚΑΙ το όνομα του χρήστη στο URL
                st.query_params["gift"] = final_reward
                st.query_params["t"] = current_ts
                st.query_params["user"] = input_name.strip()
                
                st.rerun()
    else:
        # Αν το input είναι άδειο, το κουμπί είναι κλειδωμένο (disabled) για προστασία
        st.button('GENERATE REWARD (ΠΑΡΑΚΑΛΩ ΕΙΣΑΓΕΤΕ ΟΝΟΜΑ)', disabled=True)
