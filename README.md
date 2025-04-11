# SentiFix 

**SentiFix** is an intelligent, emotion-aware service agent that processes customer queries from platforms like Email and WhatsApp. It classifies the issue using machine learning, gauges sentiment to determine urgency, generates smart responses, and assigns the ticket to the relevant support group — all through a beautiful real-time dashboard.

---

##  Key Features

-  Issue classification with ML (Login, Billing, Delivery, etc.)
-  Sentiment detection to flag urgency (Frustrated, Calm, Angry)
-  Auto-generated customer replies (GPT-like)
-  Ticket creation & team assignment
-  Real-time ticket feed on dashboard
-  Streamlit frontend for demo/demo UI

---

##  Folder Structure

```
SentiFix/
├── data/
│   └── sample_messages.csv        # Pre-labeled training data
│
├── src/
│   ├── classifier.py              # ML model training + prediction
│   ├── sentiment_analysis.py      # Emotion detection
│   ├── auto_responder.py          # GPT-like reply generator
│   ├── ticket_generator.py        # Ticket creation logic
│   └── main.py                    # Main execution script
│
├── dashboard/
│   └── app.py                     # Streamlit dashboard UI
│
├── requirements.txt
└── README.md
```

---

##  Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://gitlab.com/YOUR_USERNAME/sentifix.git
   cd sentifix
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the classifier**
   ```bash
   python src/classifier.py
   ```

4. **Launch the dashboard**
   ```bash
   streamlit run dashboard/app.py
   ```

---

## 💻 Preview

> GIFs, screenshots, and voice input demos coming soon.

---

## Roadmap

- [x] ML-based issue categorization
- [x] Sentiment & urgency detection
- [x] Auto-generated response logic
- [x] Live dashboard for tickets
- [ ] WhatsApp integration (Twilio/Meta API)
- [ ] Voice-to-text support
- [ ] Admin panel for ticket reassignment
- [ ] Deployment on cloud (Render/Heroku)

---

##  Team

Built by Bhanu Reddy and team at **Quantum Hacks 2025** 🧠🚀

---

##  License

This project is licensed under the MIT License.