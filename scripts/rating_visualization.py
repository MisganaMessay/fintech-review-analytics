import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
reviews_df = pd.read_csv(
    "data/processed/clean_reviews.csv"
)

# Average ratings
avg_ratings = reviews_df.groupby("bank")["rating"].mean()

print(avg_ratings)

# Plot
plt.figure(figsize=(8, 5))

avg_ratings.plot(
    kind="bar"
)

plt.title("Average Rating by Bank")
plt.xlabel("Bank")
plt.ylabel("Average Rating")

plt.tight_layout()

# Save
plt.savefig(
    "average_rating_by_bank.png"
)

plt.show()