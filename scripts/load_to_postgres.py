import pandas as pd

# Load processed sentiment dataset
reviews_df = pd.read_csv(
    "data/processed/reviews_with_sentiment.csv"
)

print(reviews_df.head())

print("\nDataset ready for PostgreSQL loading.")