import os
import sys
import json
import pyperclip
import streamlit as st
from streamlit_lottie import st_lottie

# Add the absolute path to the src folder
SRC_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(SRC_PATH)

# Import custom modules
from src.classifier import classify_message
from src.sentiment_analysis import analyze_sentiment
from src.auto_responder import generate_response
from src.ticket_generator import generate_ticket
from src.emailer import send_ticket_email

# Optional: Load a Lottie animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Set page config
st.set_page_config(page_title="SentiFix – AI Support Agent", layout="centered")

# Load animation
lottie_ai = load_lottiefile("dashboard/lottie_ai.json") if os.path.exists("dashboard/lottie_ai.json") else None

# Title + animation
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='color: #4A90E2; font-size: 3em;'>📬 SentiFix</h1>
        <h4 style='color: #666;'>Your AI-powered customer support assistant</h4>
    </div>
    <hr style='margin-top: -10px;'>
""", unsafe_allow_html=True)

if lottie_ai:
    st_lottie(lottie_ai, height=200, key="ai")

# Message input
st.markdown("### 💬 Paste a customer message:")
message = st.text_area("", placeholder="E.g. I was charged twice but didn’t receive anything...", height=150)

# Dark mode toggle
dark_mode = st.toggle("🌙 Enable Dark Mode")

# Analyze
analyze_clicked = st.button("🔍 Analyze & Generate Response")

if analyze_clicked and message.strip():
    category = classify_message(message)
    sentiment, polarity = analyze_sentiment(message)
    reply = generate_response(category)
    ticket = generate_ticket()

    st.markdown("### 🎟️ Ticket Info")
    st.success(f"✅ Ticket ID: `{ticket}`")
    st.info(f"📌 Issue Category: `{category}`")
    st.warning(f"⚡ Urgency Level: `{sentiment}` (Polarity: {polarity:.2f})")

    st.markdown("### 🤖 Suggested Reply")
    st.markdown(f"""
    <div style='background-color: {"#1e1e1e" if dark_mode else "#f9f9f9"}; 
                color: {"#eee" if dark_mode else "#000"}; 
                padding: 1rem; 
                border-radius: 10px; 
                border: 1px solid #ccc;'>
        {reply}
    </div>
    """, unsafe_allow_html=True)

    if st.button("📋 Copy Reply"):
        pyperclip.copy(reply)
        st.toast("Reply copied to clipboard!")

    # Email the ticket
    send_ticket_email(
        to_email="bhanureddym060305@gmail.com",  # Replace with your team email
        ticket_id=ticket,
        category=category,
        sentiment=sentiment,
        polarity=polarity,
        response=reply
    )
    st.success("📧 Ticket info emailed successfully!")

else:
    st.caption("⬆️ Enter a message and click Analyze to see results.")

# Footer
st.markdown("""---  
<div style='text-align: center; color: gray; font-size: 0.9em;'>
    Made with 💙 by <b>Bhanu</b>, <b>Darrshana</b> & <b>Anjana</b><br>
    SentiFix © 2025
</div>  
""", unsafe_allow_html=True)