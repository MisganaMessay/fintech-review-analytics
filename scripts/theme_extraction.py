import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import text

# Load cleaned reviews
reviews_df = pd.read_csv(
    "data/processed/clean_reviews.csv"
)

# Default English stopwords
english_stopwords = text.ENGLISH_STOP_WORDS

# Custom domain stopwords
custom_words = {
    "app",
    "bank",
    "banking",
    "mobile",
    "application",
    "good",
    "best",
    "nice",
    "use",
    "working",
    "ethiopia",
    "dashen",
    "boa",
    "cbe"
}

# Combine stopwords
all_stopwords = english_stopwords.union(custom_words)

banks = reviews_df["bank"].unique()

for bank in banks:

    print(f"\n========== {bank} ==========")

    bank_reviews = reviews_df[
        reviews_df["bank"] == bank
    ]["review"].astype(str)

    vectorizer = TfidfVectorizer(
        stop_words=list(all_stopwords),
        max_features=15,
        ngram_range=(1, 2),
        min_df=3
    )

    X = vectorizer.fit_transform(bank_reviews)

    keywords = vectorizer.get_feature_names_out()

    print(keywords)