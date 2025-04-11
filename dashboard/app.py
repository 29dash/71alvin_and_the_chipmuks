import os
import sys
import streamlit as st

# ✅ Print debug info to console
st.write("✅ App loaded successfully!")
print("✅ Current working dir:", os.getcwd())

# ✅ Add project root to sys.path so that 'src' can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print("✅ sys.path includes:", sys.path)

# ✅ Now import from your modules
from src.classifier import classify_message
from src.sentiment_analysis import analyze_sentiment
from src.auto_responder import generate_response
from src.ticket_generator import generate_ticket