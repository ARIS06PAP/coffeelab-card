import streamlit as st
import random
import time

# --- CONFIG ---
st.set_page_config(page_title="CoffeeLab x Aris", page_icon="☕")

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

# --- NATIVE JAVASCRIPT LOCALSTORAGE LOGIC ---

# 1. Έλεγχος αν υπάρχει ήδη αποθηκευμένο δώρο στα URL parameters (Query Params)
# Χρησιμοποιούμε τα query params ως γέφυρα μεταξύ JS και Python
query_params = st.query_params

if "gift" in query_params:
    # Αν υπάρχει στο URL, το κλειδώνουμε στην οθόνη
    saved_gift = query_params["gift"]
    st.balloons()
    st.success(f"TARGET ACQUIRED: {saved_gift}")
    st.write("---")
    st.info("Δείξε αυτή την οθόνη στον Δημήτρη ή στο ταμείο για να γίνει το redeem.")
    st.warning("🔒 Το σύστημα κλείδωσε στη συσκευή σου. Δεν επιτρέπονται επιπλέον προσπάθειες.")
    st.caption("Status: Secured | Anti-Cheat Protocol Active")

else:
    # Αν δεν υπάρχει, τρέχουμε JavaScript για να δούμε αν υπάρχει ήδη κλειδωμένο στο localStorage του browser
    # Αν βρεθεί, κάνει αυτόματα redirect το URL προσθέτοντας το δώρο
    js_script = """
    <script>
    const savedGift = localStorage.getItem("coffeelab_gift_secure");
    if (savedGift) {
        const url = new URL(window.location.href);
        if (!url.searchParams.has('gift')) {
            url.searchParams.set('gift', savedGift);
            window.location.href = url.href;
        }
    }
    </script>
    """
    st.components.v1.html(js_script, height=0)

    st.markdown("**User Verified.** Πάτα το κουμπί για να γίνει το generate του reward.")
    
    if st.button('GENERATE REWARD'):
        with st.spinner('Accessing Database...'):
            time.sleep(1)
            
            # Επιλογή δώρου
            final_reward = random.choice(rewards)
            
            # Injection JavaScript για να αποθηκευτεί ΜΟΝΙΜΑ στον browser του χρήστη
            # και να κάνει ακαριαίο reload με το κλειδωμένο query param
            js_save_and_redirect = f"""
            <script>
            localStorage.setItem("coffeelab_gift_secure", "{final_reward}");
            const url = new URL(window.location.href);
            url.searchParams.set('gift', "{final_reward}");
            window.location.href = url.href;
            </script>
            """
            st.components.v1.html(js_save_and_redirect, height=0)
            time.sleep(0.5)