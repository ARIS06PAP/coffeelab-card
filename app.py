import streamlit as st
import random
import time
from datetime import datetime

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
        font-family: monospace;
        font-size: 22px;
        font-weight: bold;
        color: #ff4b4b;
        text-align: center;
        background-color: #1a1a1a;
        padding: 12px;
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

# Αρχικοποίηση session state για τοπική ασφάλεια (πριν το refresh)
if "lock_gift" not in st.session_state:
    st.session_state.lock_gift = None
if "lock_time" not in st.session_state:
    st.session_state.lock_time = None

# Διαβάζουμε τα Query Params από το URL
query_params = st.query_params

# Καθορισμός αν ο χρήστης έχει ήδη κλειδωμένο δώρο (είτε στο URL είτε στο Session)
current_gift = query_params.get("gift", st.session_state.lock_gift)
start_timestamp = query_params.get("t", st.session_state.lock_time)

if current_gift:
    # Αν βρέθηκε δώρο, το κλειδώνουμε και στο session state για backup
    st.session_state.lock_gift = current_gift
    
    if start_timestamp is None:
        start_timestamp = int(time.time())
        st.session_state.lock_time = start_timestamp
    else:
        start_timestamp = int(start_timestamp)
        st.session_state.lock_time = start_timestamp

    # Υπολογισμός εναπομείναντος χρόνου (5 λεπτά = 300 δευτερόλεπτα)
    elapsed = int(time.time()) - start_timestamp
    remaining = 300 - elapsed

    if remaining <= 0:
        st.error("❌ ΤΟ ΚΟΥΠΟΝΙ ΕΛΗΞΕ!")
        st.warning("🔒 Το χρονικό όριο των 5 λεπτών για την εξαργύρωση παρήλθε. Η οθόνη έχει κλειδώσει.")
    else:
        st.balloons()
        st.success(f"TARGET ACQUIRED: {current_gift}")
        st.write("---")
        st.info("Δείξε αυτή την οθόνη ζωντανά στον Δημήτρη ή στο ταμείο για το redeem.")
        
        # Placeholder για το ρολόι που θα ανανεώνεται
        clock_placeholder = st.empty()
        
        # Κουμπί για χειροκίνητο refresh του χρόνου από τον Δημήτρη/Πελάτη
        st.button("🔄 ΑΝΑΝΕΩΣΗ ΩΡΑΣ / ΕΛΕΓΧΟΣ")

        # Εμφάνιση της τρέχουσας ώρας και του timer
        now = datetime.now()
        time_str = now.strftime("%H:%M:%S")
        date_str = now.strftime("%d/%m/%Y")
        
        mins, secs = divmod(remaining, 60)
        timer_str = f"{mins:02d}:{secs:02d}"
        
        clock_placeholder.markdown(f"""
            <div class="live-clock">
                📅 {date_str} — ⏰ {time_str}<br>
                <span style="color: #00ff41;">⏳ ΛΗΞΗ ΣΕ: {timer_str}</span>
            </div>
        """, unsafe_allow_html=True)

else:
    # Οθόνη παραγωγής δώρου (Αρχική κατάσταση)
    st.markdown("**User Verified.** Πάτα το κουμπί για να γίνει το generate του reward.")
    
    if st.button('GENERATE REWARD'):
        with st.spinner('Accessing Database...'):
            time.sleep(0.8)
            
            final_reward = random.choice(rewards)
            current_ts = int(time.time())
            
            # Αποθήκευση στο Session State
            st.session_state.lock_gift = final_reward
            st.session_state.lock_time = current_ts
            
            # Αποθήκευση στο URL (Query Params)
            st.query_params["gift"] = final_reward
            st.query_params["t"] = str(current_ts)
            
            st.rerun()