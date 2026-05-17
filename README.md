# Fintech Review Analytics

## Project Overview
This project analyzes Google Play Store reviews for Ethiopian banking applications:
- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

The goal is to identify customer satisfaction drivers, recurring complaints, and actionable product recommendations.

---

## Data Collection Methodology
Reviews were scraped using the `google-play-scraper` Python package.

Collected fields:
- Review text
- Rating
- Review date
- Bank name
- Source

Minimum target:
- 400 reviews per bank

---

## Preprocessing Steps
- Removed duplicate reviews
- Dropped missing values
- Standardized date format
- Saved cleaned dataset

---

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Hugging Face Transformers
- PostgreSQL
- Matplotlib
- Seaborn