import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib
import os

# Load the dataset
df = pd.read_csv("data/sample_messages.csv")ç

# Split features and labels
X = df["message"]
y = df["category"]

# Create a pipeline with text vectorizer + classifier
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Train the model
model.fit(X, y)

# Make sure the models directory exists
os.makedirs("models", exist_ok=True)

# Save the trained model
joblib.dump(model, "models/classifier.pkl")

print("✅ Model trained and saved to models/classifier.pkl")
