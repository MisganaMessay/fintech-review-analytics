import pandas as pd
from google_play_scraper import reviews, Sort

apps = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

all_reviews = []

for bank, package in apps.items():
    result, _ = reviews(
        package,
        lang='en',
        country='et',
        sort=Sort.NEWEST,
        count=500
    )

    for review in result:
        all_reviews.append({
            'review_id': review.get('reviewId'),
            'review': review.get('content'),
            'rating': review.get('score'),
            'date': review.get('at'),
            'bank': bank,
            'source': 'Google Play'
        })

reviews_df = pd.DataFrame(all_reviews)

reviews_df.to_csv('data/raw/raw_reviews.csv', index=False)

print(reviews_df.head())
print(reviews_df.shape)