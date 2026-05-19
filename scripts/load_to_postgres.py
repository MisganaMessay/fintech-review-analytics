import pandas as pd
import psycopg2

# Database connection
conn = psycopg2.connect(
    host="localhost",
    database="fintech_reviews",
    user="postgres",
    password="12345678"
)

cur = conn.cursor()

# Load dataset
df = pd.read_csv("data/processed/reviews_with_sentiment.csv")

# Insert banks
banks = df["bank"].unique()

for bank in banks:
    cur.execute(
        """
        INSERT INTO banks (bank_name)
        VALUES (%s)
        ON CONFLICT (bank_name) DO NOTHING
        """,
        (bank,)
    )

conn.commit()

# Get bank ids
cur.execute("SELECT bank_id, bank_name FROM banks")
bank_map = {name: bid for bid, name in cur.fetchall()}

# Insert reviews
for _, row in df.iterrows():
    cur.execute(
        """
        INSERT INTO reviews (
            bank_id,
            review_text,
            rating,
            review_date,
            sentiment_label,
            sentiment_score
        )
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (
            bank_map[row["bank"]],
            row["review"],
            int(row["rating"]),
            None,
            row["sentiment_label"],
            float(row["sentiment_score"])
        )
    )

conn.commit()

print("Data loaded successfully into PostgreSQL.")

cur.close()
conn.close()