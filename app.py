import streamlit as st
import random
import time
from streamlit_local_storage import LocalStorage

# --- CONFIG ---
st.set_page_config(page_title="CoffeeLab x Aris", page_icon="☕")

# Αρχικοποίηση Local Storage για να αποθηκεύουμε στο κινητό του χρήστη
local_storage = LocalStorage()

# CSS για Clean & Dark look
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

# Μικρό delay για να προλάβει να διαβάσει ο browser το local storage
time.sleep(0.3)

# Έλεγχος αν υπάρχει ήδη αποθηκευμένο δώρο στη μνήμη της συσκευής
saved_reward = local_storage.getItem("coffeelab_gift")

if saved_reward is None:
    st.markdown("**User Verified.** Πάτα το κουμπί για να γίνει το generate του reward.")
    
    if st.button('GENERATE REWARD'):
        with st.spinner('Accessing Database...'):
            time.sleep(1.2)
            
            # Επιλογή και άμεση αποθήκευση στο κινητό του χρήστη
            final_reward = random.choice(rewards)
            local_storage.setItem("coffeelab_gift", final_reward)
            
            # Rerun για να ανανεωθεί το UI με το κλειδωμένο δώρο
            st.rerun()
else:
    # Αν ο χρήστης έχει ήδη δώρο (ακόμα και μετά από refresh), του δείχνει μόνο αυτό
    st.balloons()
    st.success(f"TARGET ACQUIRED: {saved_reward}")
    
    st.write("---")
    st.info("Δείξε αυτή την οθόνη στον Δημήτρη ή στο ταμείο για να γίνει το redeem.")
    st.warning("🔒 Το σύστημα κλείδωσε στη συσκευή σου. Δεν επιτρέπονται επιπλέον προσπάθειες.")
    st.caption(f"Status: Secured | Anti-Cheat Protocol Active")