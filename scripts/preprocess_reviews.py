import pandas as pd

# Load raw data
reviews_df = pd.read_csv("data/raw/raw_reviews.csv")

print("Initial Shape:", reviews_df.shape)

# Remove duplicates
reviews_df = reviews_df.drop_duplicates(subset=["review_id"])

# Remove missing values
reviews_df = reviews_df.dropna(subset=["review", "rating"])

# Format dates
reviews_df["date"] = pd.to_datetime(
    reviews_df["date"]
).dt.strftime("%Y-%m-%d")

# Keep required columns
reviews_df = reviews_df[
    [
        "review",
        "rating",
        "date",
        "bank",
        "source"
    ]
]

print("Cleaned Shape:", reviews_df.shape)

# Save cleaned data
reviews_df.to_csv(
    "data/processed/clean_reviews.csv",
    index=False
)

print("Preprocessing completed successfully.")