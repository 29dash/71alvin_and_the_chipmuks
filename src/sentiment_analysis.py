from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity < -0.3:
        return "Urgent", polarity
    elif polarity > 0.3:
        return "Low", polarity
    else:
        return "Normal", polarity