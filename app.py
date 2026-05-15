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
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ System Access Granted (Debug Mode)")
st.subheader("CoffeeLab x Aris Project")
st.write("---")

rewards = [
    "🎁 1+1 Καφές (Optimization Protocol)",
    "🎁 -20% στην επόμενη παραγγελία",
    "🎁 Δωρεάν Snack / Cookie",
    "🎁 Upgrade σε Large μέγεθος",
    "🎁 Free Extra Shot (Energy Boost)"
]
reward_weights = [5, 15, 15, 32.5, 32.5]

query_params = st.query_params

if "gift" in query_params:
    saved_gift = query_params["gift"]
    user_name = query_params.get("user", "Agent")
    start_ts = query_params["t"]

    st.balloons()
    st.success(f"TARGET ACQUIRED: {user_name} -> {saved_gift}")
    st.write("---")
    
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
            const timerStr = (hours < 10 ? "0" : "") + hours + ":" + (minutes < 10 ? "0" : "") + minutes + ":" + (seconds < 10 ? "0" : "") + seconds;
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
    st.markdown("**User Verification Required.**")
    input_name = st.text_input("Πληκτρολόγησε το Όνομα ή το Instagram σου για να ξεκλειδώσεις το reward:", "")
    st.write("---")
    
    if input_name.strip() != "":
        st.markdown("✅ *Στοιχεία έγκυρα. Το σύστημα είναι έτοιμο.*")
        
        if st.button('GENERATE REWARD'):
            with st.spinner('Securing Connection & Generating Reward...'):
                
                final_reward = random.choices(rewards, weights=reward_weights, k=1)[0]
                current_ts = str(int(time.time()))
                
                # Απευθείας εκτέλεση χωρίς try/except για να δούμε το error
                conn = st.connection("gsheets", type=st.ServiceConnection)
                
                tz = zoneinfo.ZoneInfo("Europe/Athens")
                now_gr = datetime.now(tz)
                date_str = now_gr.strftime("%d/%m/%Y")
                time_str = now_gr.strftime("%H:%M:%S")
                
                new_row = {
                    "Date": date_str,
                    "Time": time_str,
                    "User": input_name.strip(),
                    "Reward": final_reward
                }
                
                conn.create(data=[new_row])

                st.query_params["gift"] = final_reward
                st.query_params["t"] = current_ts
                st.query_params["user"] = input_name.strip()
                
                st.rerun()
    else:
        st.button('GENERATE REWARD (ΠΑΡΑΚΑΛΩ ΕΙΣΑΓΕΤΕ ΟΝΟΜΑ)', disabled=True)
