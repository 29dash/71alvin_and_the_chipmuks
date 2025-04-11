import os
import sys
import streamlit as st

# Set page config FIRST before any other Streamlit calls
st.set_page_config(page_title="SentiFix", page_icon="📬", layout="centered")

# Print debug info to console (only using `print`, not `st.write`)
print("App loaded successfully!")
print("Current working dir:", os.getcwd())

# Add project root to sys.path so that 'src' can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print("sys.path includes:", sys.path)

# Now import from your modules
from src.classifier import classify_message
from src.sentiment_analysis import analyze_sentiment
from src.auto_responder import generate_response
from src.ticket_generator import generate_ticket

# Now you're safe to start using other `st.` commands
st.title("📬 SentiFix – AI Customer Support Assistant")
st.markdown("Let our AI handle complaints, emotions, and smart replies in one click.")
