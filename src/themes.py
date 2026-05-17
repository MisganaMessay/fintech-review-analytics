from sklearn.feature_extraction.text import TfidfVectorizer


def extract_keywords(texts, top_n=10):
    vectorizer = TfidfVectorizer(
        stop_words='english',
        ngram_range=(1, 2),
        max_features=100
    )

    X = vectorizer.fit_transform(texts)

    keywords = vectorizer.get_feature_names_out()

    return keywords[:top_n]