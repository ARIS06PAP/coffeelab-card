# ======================================================
# SETUP INSTRUCTIONS (CONDA):
# 1. conda activate coffeelab_env
# 2. streamlit run app.py
# ======================================================

import streamlit as st
import random
import time

# Ρυθμίσεις Σελίδας
st.set_page_config(page_title="CoffeeLab Mystery", page_icon="☕")

# CSS για να "κρύψουμε" το menu του Streamlit και να φαίνεται σαν native app
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stButton>button {
                width: 100%;
                border-radius: 20px;
                height: 3em;
                background-color: #E63946;
                color: white;
                font-weight: bold;
            }
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Main UI
st.title("🎯 Βρήκες τον Δημήτρη!")
st.write("---")

st.info("Σκάναρες την κάρτα επιτυχώς. Πάτα το κουμπί για να δεις τι κέρδισες!")

rewards = [
    "☕ Δωρεάν αναβάθμιση σε Large μέγεθος",
    "🥐 1+1 σε όλα τα σφολιατοειδή",
    "🍩 Δώρο ένα Donut με τον καφέ σου",
    "💸 -1€ στην επόμενη παραγγελία",
    "🥤 Δωρεάν νερό 500ml"
]

if st.button('ΑΠΟΚΑΛΥΨΗ ΔΩΡΟΥ 🎁'):
    # Animation αναμονής
    progress_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        progress_bar.progress(percent_complete + 1)
    
    selected_reward = random.choice(rewards)
    
    st.balloons()
    st.success("ΚΕΡΔΙΣΕΣ!")
    st.header(selected_reward)
    
    st.markdown("---")
    st.caption("Δείξε αυτή την οθόνη στον barista για την εξαργύρωση.")
    st.caption(f"Timestamp: {time.strftime('%H:%M:%S')}")