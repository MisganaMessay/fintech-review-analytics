import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
reviews_df = pd.read_csv(
    "data/processed/reviews_with_sentiment.csv"
)

# Plot
plt.figure(figsize=(10, 6))

sns.countplot(
    data=reviews_df,
    x="bank",
    hue="sentiment_label"
)

plt.title("Sentiment Distribution by Bank")
plt.xlabel("Bank")
plt.ylabel("Number of Reviews")

plt.tight_layout()

plt.savefig(
    "sentiment_distribution.png"
)

plt.show()