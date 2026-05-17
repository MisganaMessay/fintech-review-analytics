import pandas as pd
from google_play_scraper import Sort, reviews, app
import os

# UPDATED App IDs for the three banks
apps = {
    "CBE": "com.cbe.mobilebanking",           # Main CBE App
    "BOA": "com.bankofabyssinia.boamobile.retail", # Newest BOA Retail App
    "Dashen": "et.com.dashenbank.amole"       # Dashen Amole
}

def main():
    all_data = []
    
    for bank_name, app_id in apps.items():
        print(f"\n--- Checking {bank_name} ({app_id}) ---")
        try:
            # Step 1: Check if app is even reachable
            info = app(app_id)
            print(f"Found App: {info['title']} by {info['developer']}")
            
            # Step 2: Scrape reviews (trying No Country filter first for better reach)
            result, _ = reviews(
                app_id,
                lang='en',
                sort=Sort.NEWEST,
                count=200
            )
            
            if result:
                df = pd.DataFrame(result)
                df = df[['content', 'score', 'at', 'reviewId']]
                df.columns = ['review', 'rating', 'date', 'id']
                df['bank'] = bank_name
                df['source'] = 'Google Play'
                all_data.append(df)
                print(f"SUCCESS: Collected {len(df)} reviews.")
            else:
                print(f"FAILED: No reviews returned for {bank_name}")

        except Exception as e:
            print(f"ERROR: Could not find app or connect: {e}")

    if all_data:
        final_df = pd.concat(all_data, ignore_index=True)
        final_df['date'] = pd.to_datetime(final_df['date']).dt.strftime('%Y-%m-%d')
        os.makedirs('data/raw', exist_ok=True)
        final_df.to_csv('data/raw/reviews.csv', index=False)
        print(f"\nDONE: Saved {len(final_df)} reviews to data/raw/reviews.csv")
    else:
        print("\nSCRAPER FAILED. Moving to Track B (Manual Data Entry).")

if __name__ == "__main__":
    main()