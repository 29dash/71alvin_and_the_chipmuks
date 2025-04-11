from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity < -0.3:
        return "Urgent"
    elif polarity > 0.3:
        return "Low"
    else:
        return "Normal"