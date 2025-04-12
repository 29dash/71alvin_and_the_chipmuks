import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import os

df = pd.read_csv("data/sample_messages.csv")
X = df["message"]
y = df["category"]

# Create components
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_vectorized, y)

# Save both separately
os.makedirs("models", exist_ok=True)
joblib.dump(vectorizer, "models/vectorizer.pkl")
joblib.dump(model, "models/model.pkl")

print("✅ Vectorizer and model saved separately!")
