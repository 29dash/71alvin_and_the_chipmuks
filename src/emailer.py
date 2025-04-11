import smtplib
from email.message import EmailMessage

def send_ticket_email(to_email, ticket_id, category, sentiment, polarity, response):
    msg = EmailMessage()
    msg['Subject'] = f"New SentiFix Ticket - {ticket_id}"
    msg['From'] = 'bhanureddym060305@gmail.com'
    msg['To'] = to_email

    msg.set_content(f"""
🧠 Category: {category}
⚡ Sentiment: {sentiment} (Polarity: {polarity:.2f})
💬 Response: {response}
🎟️ Ticket ID: {ticket_id}
    """)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('bhanureddym060305@gmail.com', 'woha idpw airo bsje')
        smtp.send_message(msg)