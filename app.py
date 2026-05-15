import streamlit as st
import random
import time
from datetime import datetime
import zoneinfo

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
    .live-clock {
        font-size: 24px;
        font-weight: bold;
        color: #ff4b4b;
        text-align: center;
        background-color: #1a1a1a;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #ff4b4b;
        margin-bottom: 15px;
    }
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

# 1. Έλεγχος αν υπάρχει ήδη κλειδωμένο δώρο στο URL
if "gift" in st.query_params:
    saved_gift = st.query_params["gift"]
    
    # Διαχείριση Χρονικού Ορίου (Timestamp εξαργύρωσης)
    if "t" not in st.query_params:
        # Αν για κάποιο λόγο δεν υπάρχει timestamp, βάζουμε το τρέχον
        st.query_params["t"] = str(int(time.time()))
    
    start_time = int(st.query_params["t"])
    current_time = int(time.time())
    elapsed_time = current_time - start_time
    remaining_time = 300 - elapsed_time # 300 δευτερόλεπτα = 5 λεπτά

    if remaining_time <= 0:
        st.error("❌ Το κουπόνι έληξε!")
        st.warning("🔒 Το χρονικό όριο των 5 λεπτών για την εξαργύρωση παρήλθε. Η οθόνη έχει κλειδώσει.")
    else:
        st.balloons()
        st.success(f"TARGET ACQUIRED: {saved_gift}")
        
        # Live Component για το Ρολόι και το Timer (χρησιμοποιεί infinite loop με sleep)
        clock_placeholder = st.empty()
        
        st.write("---")
        st.info("Δείξε αυτή την οθόνη ζωντανά στον Δημήτρη ή στο ταμείο για το redeem.")
        
        # 🔄 Loop που ανανεώνει το ρολόι κάθε δευτερόλεπτο χωρίς rerun όλης της σελίδας
        while remaining_time > 0:
            # Σωστή ώρα Ελλάδας
            tz = zoneinfo.ZoneInfo("Europe/Athens")
            now = datetime.now(tz)
            time_str = now.strftime("%H:%M:%S")
            date_str = now.strftime("%d/%m/%Y")
            
            mins, secs = divmod(remaining_time, 60)
            timer_str = f"{mins:02d}:{secs:02d}"
            
            # Injection του Live UI
            clock_placeholder.markdown(f"""
                <div class="live-clock">
                    📅 {date_str} — ⏰ {time_str}<br>
                    ⏳ Λήξη κουπονιού σε: {timer_str}
                </div>
            """, unsafe_allow_html=True)
            
            time.sleep(1)
            remaining_time -= 1
            
        # Μόλις τελειώσει το loop (λήξει ο χρόνος) κάνουμε rerun για να δείξει το error screen
        st.rerun()

else:
    # Αν δεν υπάρχει δώρο, δείχνουμε το κουμπί
    st.markdown("**User Verified.** Πάτα το κουμπί για να γίνει το generate του reward.")
    
    if st.button('GENERATE REWARD'):
        with st.spinner('Accessing Database...'):
            time.sleep(0.8)
            
            final_reward = random.choice(rewards)
            
            # Κλειδώνουμε το δώρο ΚΑΙ το τρέχον timestamp (epoch time) στα query params
            st.query_params["gift"] = final_reward
            st.query_params["t"] = str(int(time.time()))
            
            # Backup στο localStorage
            js_save = f"""
            <script>
            localStorage.setItem("coffeelab_secure_final", "{final_reward}");
            </script>
            """
            st.components.v1.html(js_save, height=0)
            st.rerun()

# Backup check αν ο χρήστης πειράξει το URL
js_backup_check = """
<script>
const fallback = localStorage.getItem("coffeelab_secure_final");
const urlParams = new URLSearchParams(window.location.search);
if (fallback && !urlParams.has('gift')) {
    const currentUrl = new URL(window.location.href);
    currentUrl.searchParams.set('gift', fallback);
    window.location.href = currentUrl.href;
}
</script>
"""
st.components.v1.html(js_backup_check, height=0)