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
    
    /* Στυλ για το Live Ρολόι και το Timer μέσω JS */
    .clock-container {
        font-family: monospace;
        font-size: 20px;
        font-weight: bold;
        color: #ff4b4b;
        text-align: center;
        background-color: #1a1a1a;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #ff4b4b;
        margin-top: 15px;
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
    
    st.balloons()
    st.success(f"TARGET ACQUIRED: {saved_gift}")
    
    # Εισαγωγή του Live Ρολογιού και του 5-minute Countdown μέσω HTML/JavaScript
    # Αυτό το κομμάτι τρέχει live στον browser χωρίς να κολλάει την Python
    js_countdown_clock = """
    <div id="clock-box" class="clock-container">
        Loading Security Protocols...
    </div>

    <script>
    // 1. Ρύθμιση του Target Time (5 λεπτά από την πρώτη στιγμή που φορτώνει η σελίδα με το δώρο)
    let startTime = localStorage.getItem("coffeelab_start_time");
    if (!startTime) {
        startTime = Math.floor(Date.now() / 1000);
        localStorage.setItem("coffeelab_start_time", startTime);
    }

    function updateClock() {
        const now = new Date();
        const currentTimestamp = Math.floor(Date.now() / 1000);
        
        // Μορφοποίηση Ώρας Ελλάδας
        const timeStr = now.toLocaleTimeString('el-GR', { hour12: false });
        const dateStr = now.toLocaleDateString('el-GR');
        
        // Υπολογισμός Αντίστροφης Μέτρησης (300 δευτερόλεπτα = 5 λεπτά)
        const elapsedTime = currentTimestamp - parseInt(startTime);
        const remainingTime = 300 - elapsedTime;
        
        const clockBox = document.getElementById("clock-box");
        
        if (remainingTime <= 0) {
            clockBox.innerHTML = "❌ ΤΟ ΚΟΥΠΟΝΙ ΕΛΗΞΕ!<br><span style='font-size:14px; color:gray;'>🔒 Το χρονικό όριο των 5 λεπτών παρήλθε.</span>";
            clockBox.style.borderColor = "#gray";
            clockBox.style.color = "#ff4b4b";
        } else {
            const minutes = Math.floor(remainingTime / 60);
            const seconds = remainingTime % 60;
            const timerStr = (minutes < 10 ? "0" : "") + minutes + ":" + (seconds < 10 ? "0" : "") + seconds;
            
            clockBox.innerHTML = "📅 " + dateStr + " — ⏰ " + timeStr + "<br><span style='color:#00ff41;'>⏳ ΛΗΞΗ ΣΕ: " + timerStr + "</span>";
        }
    }

    // Ανανέωση κάθε 1 δευτερόλεπτο
    setInterval(updateClock, 1000);
    updateClock();
    </script>
    """
    st.components.v1.html(js_countdown_clock, height=120)
    
    st.write("---")
    st.info("Δείξε αυτή την οθόνη ζωντανά στον Δημήτρη ή στο ταμείο για το redeem.")
    st.warning("🔒 Το σύστημα κλείδωσε. Δεν επιτρέπονται επιπλέον προσπάθειες.")

else:
    # Αν δεν υπάρχει δώρο, δείχνουμε το κουμπί κανονικά
    st.markdown("**User Verified.** Πάτα το κουμπί για να γίνει το generate του reward.")
    
    if st.button('GENERATE REWARD'):
        with st.spinner('Accessing Database...'):
            time.sleep(0.8)
            
            final_reward = random.choice(rewards)
            
            # Κλειδώνουμε το δώρο στα query params
            st.query_params["gift"] = final_reward
            
            # Backup στο localStorage για το Anti-Cheat
            js_save = f"""
            <script>
            localStorage.setItem("coffeelab_secure_final", "{final_reward}");
            localStorage.setItem("coffeelab_start_time", Math.floor(Date.now() / 1000));
            </script>
            """
            st.components.v1.html(js_save, height=0)
            st.rerun()

# 2. Backup έλεγχος σε περίπτωση που ο χρήστης έσβησε το URL αλλά το έχει στο localStorage
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