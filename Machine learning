from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# For vectorization
newdf = dat2[["title", "tags", "thumbnail"]]
cv = CountVectorizer(max_features=5000, stop_words="english")
vec = cv.fit_transform(newdf["tags"]).toarray()

# Calculate similarity
similarity = cosine_similarity(vec)

# Recommendation logic
def recommender(book_title):
    if book_title not in newdf["title"].values:
        return []
    index = newdf[newdf["title"] == book_title].index[0]
    distances = similarity[index]
    book_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [newdf.iloc[i[0]] for i in book_list]
