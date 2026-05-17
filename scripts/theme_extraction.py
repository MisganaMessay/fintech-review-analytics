import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load data
reviews_df = pd.read_csv(
    "data/processed/clean_reviews.csv"
)

# Separate by bank
banks = reviews_df["bank"].unique()

for bank in banks:

    print(f"\nTop keywords for {bank}")

    bank_reviews = reviews_df[
        reviews_df["bank"] == bank
    ]["review"].astype(str)

    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=10,
        ngram_range=(1, 2)
    )

    X = vectorizer.fit_transform(bank_reviews)

    keywords = vectorizer.get_feature_names_out()

    print(keywords)