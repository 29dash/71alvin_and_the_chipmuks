import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import os

def train_classifier():
    df = pd.read_csv('data/sample_messages.csv')
    tfidf = TfidfVectorizer()
    X = tfidf.fit_transform(df['message'])
    y = df['category']

    model = MultinomialNB()
    model.fit(X, y)

    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/classifier.pkl')
    joblib.dump(tfidf, 'models/vectorizer.pkl')
    print("✅ Model trained and saved!")

def classify_message(msg):
    model = joblib.load('models/classifier.pkl')
    vectorizer = joblib.load('models/vectorizer.pkl')
    X = vectorizer.transform([msg])
    return model.predict(X)[0]

# Run this to train
if __name__ == "__main__":
    train_classifier()