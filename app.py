import streamlit as st
import random
import time

# --- CONFIG ---
st.set_page_config(page_title="CoffeeLab x Aris", page_icon="☕")

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

rewards = [
    "🎁 1+1 Καφές (Optimization Protocol)",
    "🎁 -20% στην επόμενη παραγγελία",
    "🎁 Δωρεάν Snack / Cookie",
    "🎁 Upgrade σε Large μέγεθος",
    "🎁 Free Extra Shot (Energy Boost)"
]

# Διαβάζουμε τα Query Params από το URL
query_params = st.query_params

if "gift" in query_params:
    saved_gift = query_params["gift"]
    
    # Αν δεν υπάρχει timestamp έναρξης στο URL, βάζουμε το τρέχον
    if "t" not in query_params:
        st.query_params["t"] = str(int(time.time()))
    
    start_ts = query_params["t"]

    st.balloons()
    st.success(f"TARGET ACQUIRED: {saved_gift}")
    st.write("---")
    st.info("Δείξε αυτή την οθόνη ζωντανά στον Δημήτρη ή στο ταμείο για το redeem.")

    # 🕒 LIVE EMBEDDED CLOCK VIA HTML/JS (No cross-origin storage issues)
    # Περνάμε το start_ts απευθείας μέσα στο script για να υπολογίζει το 24ωρο
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
    
    function updateClock() {
        const now = new Date();
        const currentTimestamp = Math.floor(Date.now() / 1000);
        
        // 1. Μορφοποίηση Τρέχουσας Ώρας
        const timeStr = now.toLocaleTimeString('el-GR', { hour12: false });
        const dateStr = now.toLocaleDateString('el-GR');
        
        // 2. Υπολογισμός Αντίστροφης Μέτρησης 24 Ωρών (24 * 3600 = 86400 δευτερόλεπτα)
        const elapsedTime = currentTimestamp - startTimestamp;
        const remainingTime = 86400 - elapsedTime;
        
        const box = document.getElementById("countdown-box");
        
        if (remainingTime <= 0) {
            box.innerHTML = "❌ ΤΟ ΚΟΥΠΟΝΙ ΕΛΗΞΕ!<br><span style='font-size:14px; color:gray;'>🔒 Το χρονικό όριο των 24 ωρών παρήλθε.</span>";
            box.style.borderColor = "gray";
            box.style.color = "#ff4b4b";
        } else {
            // Μετατροπή δευτερολέπτων σε Ώρες:Λεπτά:Δευτερόλεπτα
            const hours = Math.floor(remainingTime / 3600);
            const minutes = Math.floor((remainingTime % 3600) / 60);
            const seconds = remainingTime % 60;
            
            const timerStr = 
                (hours < 10 ? "0" : "") + hours + ":" + 
                (minutes < 10 ? "0" : "") + minutes + ":" + 
                (seconds < 10 ? "0" : "") + seconds;
            
            box.innerHTML = "📅 " + dateStr + " — ⏰ " + timeStr + "<br><span style='color:#00ff41;'>⏳ ΛΗΞΗ ΣΕ: " + timerStr + "</span>";
        }
    }

    // Εκτέλεση και ανανέωση ανά δευτερόλεπτο
    setInterval(updateClock, 1000);
    updateClock();
    </script>
    """
    st.components.v1.html(live_clock_html, height=120)
    st.warning("🔒 Το σύστημα κλείδωσε. Δεν επιτρέπονται επιπλέον προσπάθειες.")

else:
    # Αρχική οθόνη με το κουμπί
    st.markdown("**User Verified.** Πάτα το κουμπί για να γίνει το generate του reward.")
    
    if st.button('GENERATE REWARD'):
        with st.spinner('Accessing Database...'):
            time.sleep(0.8)
            
            final_reward = random.choice(rewards)
            current_ts = str(int(time.time()))
            
            # Κλειδώνουμε το δώρο και το timestamp στο URL
            st.query_params["gift"] = final_reward
            st.query_params["t"] = current_ts
            
            st.rerun()
