import pandas as pd
from transformers import pipeline

# Load dataset
reviews_df = pd.read_csv('data/processed/clean_reviews.csv')

# Load sentiment model
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

sentiments = []

for review in reviews_df['review']:
    try:
        result = classifier(review[:512])[0]

        sentiments.append({
            'sentiment_label': result['label'],
            'sentiment_score': result['score']
        })

    except:
        sentiments.append({
            'sentiment_label': 'NEUTRAL',
            'sentiment_score': 0.0
        })

sentiment_df = pd.DataFrame(sentiments)

reviews_df = pd.concat([reviews_df, sentiment_df], axis=1)

reviews_df.to_csv(
    'data/processed/reviews_with_sentiment.csv',
    index=False
)

print(reviews_df.head())