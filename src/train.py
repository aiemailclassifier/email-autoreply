import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
from preprocess import clean_text

# Load data
df = pd.read_csv('data/emails.csv')
df['text'] = df['subject'] + ' ' + df['body']
df['text_clean'] = df['text'].apply(clean_text)

# Train-test split
from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(df['text_clean'], df['theme'], test_size=0.2, random_state=42)

# Build pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression(max_iter=1000))
])

pipeline.fit(X_train, y_train)

# Evaluate
print("Validation accuracy:", pipeline.score(X_val, y_val))

# Save model
joblib.dump(pipeline, 'models/theme_classifier.pkl')
