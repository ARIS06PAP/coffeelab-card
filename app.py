import streamlit as st
import random
import time
from datetime import datetime
import zoneinfo
import requests # Χρειάζεται μόνο αυτή η βιβλιοθήκη

# --- CONFIG ---
st.set_page_config(page_title="CoffeeLab x Aris", page_icon="☕")

# ΒΑΛΕ ΕΔΩ ΤΟ URL ΠΟΥ ΕΚΑΝΕΣ COPY ΑΠΟ ΤΟ GOOGLE SCRIPT
SCRIPT_URL = "https://docs.google.com/spreadsheets/d/1YVXYNAmITQrGrmRvQ8a1ef4-F6dQZPjp8-PAr4wbyk4/edit?usp=sharing" 

st.markdown("<style>.stApp { background-color: #050505; } .stButton>button { width: 100%; height: 3.5em; background-color: #00ff41; color: black; font-weight: bold; }</style>", unsafe_allow_html=True)

st.title("⚡ System Access Granted")
st.write("---")

rewards = ["🎁 1+1 Καφές", "🎁 -20% Έκπτωση", "🎁 Δωρεάν Snack", "🎁 Upgrade Size", "🎁 Free Extra Shot"]
reward_weights = [5, 15, 15, 32.5, 32.5]

query_params = st.query_params

if "gift" in query_params:
    st.balloons()
    st.success(f"TARGET ACQUIRED: {query_params['user']} -> {query_params['gift']}")
    st.warning("🔒 Το σύστημα κλείδωσε για 24 ώρες.")
else:
    input_name = st.text_input("Όνομα / Instagram:", "")
    if input_name.strip() != "":
        if st.button('GENERATE REWARD'):
            with st.spinner('Sending Data...'):
                final_reward = random.choices(rewards, weights=reward_weights, k=1)[0]
                
                # Προετοιμασία Δεδομένων
                tz = zoneinfo.ZoneInfo("Europe/Athens")
                now_gr = datetime.now(tz)
                
                payload = {
                    "Date": now_gr.strftime("%d/%m/%Y"),
                    "Time": now_gr.strftime("%H:%M:%S"),
                    "User": input_name.strip(),
                    "Reward": final_reward
                }
                
                # ΑΠΟΣΤΟΛΗ ΣΤΟ GOOGLE SHEET (χωρίς καμία άλλη βιβλιοθήκη)
                try:
                    requests.post(SCRIPT_URL, json=payload)
                except:
                    pass # Fail-safe για να πάρει το δώρο ο πελάτης

                st.query_params["gift"] = final_reward
                st.query_params["t"] = str(int(time.time()))
                st.query_params["user"] = input_name.strip()
                st.rerun()
