# ======================================================
# SETUP INSTRUCTIONS (CONDA):
# 1. conda activate aris
# 2. streamlit run app.py
# ======================================================

import streamlit as st
import random
import time

# --- CONFIG ---
st.set_page_config(page_title="CoffeeLab x Aris", page_icon="⚡")

# CSS για Clean & Dark look (Engineering Style)
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    .stButton>button {
        width: 100%;
        height: 3.5em;
        background-color: #00ff41; /* Matrix Green */
        color: black;
        font-weight: bold;
        border: none;
        text-transform: uppercase;
    }
    .stSuccess { background-color: #1e1e1e; color: #00ff41; border: 1px solid #00ff41; }
    </style>
    """, unsafe_allow_html=True)

# --- APP LOGIC ---
st.title("⚡ System Access Granted")
st.subheader("CoffeeLab x Aris Project")
st.write("---")

# Λίστα δώρων
rewards = [
    "🎁 1+1 Καφές (Optimization Protocol)",
    "🎁 -20% στην επόμενη παραγγελία",
    "🎁 Δωρεάν Snack / Cookie",
    "🎁 Upgrade σε Large μέγεθος",
    "🎁 Free Extra Shot (Energy Boost)"
]

# Αρχικοποίηση του session_state αν δεν υπάρχει ήδη
if 'reward_generated' not in st.session_state:
    st.session_state.reward_generated = False
if 'user_reward' not in st.session_state:
    st.session_state.user_reward = None

# Έλεγχος αν ο χρήστης έχει ήδη πάρει δώρο
if not st.session_state.reward_generated:
    st.markdown("**User Verified.** Πάτα το κουμπί για να γίνει το generate του reward.")
    
    if st.button('GENERATE REWARD'):
        with st.spinner('Accessing Database...'):
            time.sleep(1.2) # Εφέ για το σασπένς
            
            # Επιλογή δώρου και αποθήκευση στο session_state
            st.session_state.user_reward = random.choice(rewards)
            st.session_state.reward_generated = True
            
            # Αναγκαστικό rerun για να κλειδώσει το UI
            st.rerun()

else:
    # Αν έχει ήδη δημιουργηθεί δώρο, δείχνει ΜΟΝΟ αυτό, χωρίς κουμπί
    st.balloons()
    st.success(f"TARGET ACQUIRED: {st.session_state.user_reward}")
    
    st.write("---")
    st.info("Δείξε αυτή την οθόνη στον Δημήτρη ή στο ταμείο για να γίνει το redeem.")
    st.warning("🔒 Το σύστημα κλείδωσε. Δεν επιτρέπονται επιπλέον προσπάθειες.")
    st.caption(f"Status: Validated | Session Secured")