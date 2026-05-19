import matplotlib.pyplot as plt

# Example keywords from analysis
keywords = {
    "fast": 18,
    "easy": 15,
    "update": 14,
    "problem": 13,
    "transfer": 11,
    "slow": 10,
    "friendly": 9
}

# Plot
plt.figure(figsize=(10, 5))

plt.bar(
    keywords.keys(),
    keywords.values()
)

plt.title("Top Review Keywords")
plt.xlabel("Keywords")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig(
    "keyword_frequency.png"
)
plt.savefig("theme_frequency.png")
plt.show()