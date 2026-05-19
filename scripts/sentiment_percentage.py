import pandas as pd
import matplotlib.pyplot as plt

# Load sentiment data
reviews_df = pd.read_csv(
    "data/processed/reviews_with_sentiment.csv"
)

# Calculate percentages
sentiment_counts = (
    reviews_df
    .groupby(["bank", "sentiment_label"])
    .size()
    .unstack(fill_value=0)
)

sentiment_percentages = (
    sentiment_counts.div(
        sentiment_counts.sum(axis=1),
        axis=0
    ) * 100
)

print(sentiment_percentages)

# Plot
sentiment_percentages.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Sentiment Percentage by Bank")
plt.xlabel("Bank")
plt.ylabel("Percentage")

plt.tight_layout()

plt.savefig(
    "sentiment_percentage.png"
)

plt.show()