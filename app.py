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

# 1. Έλεγχος αν υπάρχει ήδη κλειδωμένο δώρο στο URL (Query Params)
if "gift" in st.query_params:
    saved_gift = st.query_params["gift"]
    st.balloons()
    st.success(f"TARGET ACQUIRED: {saved_gift}")
    st.write("---")
    st.info("Δείξε αυτή την οθόνη στον Δημήτρη ή στο ταμείο για να γίνει το redeem.")
    st.warning("🔒 Το σύστημα κλείδωσε. Δεν επιτρέπονται επιπλέον προσπάθειες.")
    st.caption("Status: Secured | Anti-Cheat Protocol Active")

else:
    # Αν δεν υπάρχει, δείχνουμε ΚΑΝΟΝΙΚΑ το κουμπί
    st.markdown("**User Verified.** Πάτα το κουμπί για να γίνει το generate του reward.")
    
    if st.button('GENERATE REWARD'):
        with st.spinner('Accessing Database...'):
            time.sleep(0.8)
            
            # Επιλογή δώρου
            final_reward = random.choice(rewards)
            
            # Κλειδώνουμε το δώρο στα query params του Streamlit (Native Python)
            st.query_params["gift"] = final_reward
            
            # Εκτελούμε ένα απλό JavaScript injection ΜΟΝΟ για να αποθηκευτεί στον browser για το μέλλον
            js_save = f"""
            <script>
            localStorage.setItem("coffeelab_secure_final", "{final_reward}");
            </script>
            """
            st.components.v1.html(js_save, height=0)
            
            # Force ανανέωση για να διαβάσει το νέο URL param
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