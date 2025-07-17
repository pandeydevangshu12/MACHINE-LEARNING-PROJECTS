import pandas as pd

# Load dataset
dat2 = pd.read_csv("Books.csv")

# Drop unnecessary columns and handle missing data
dat2.drop(["pages", "published_date", "publisher", "language", "average_rating", "ratings_count"], axis=1, inplace=True)
dat2.fillna("", inplace=True)

# Data cleaning
dat2["genre"] = dat2["genre"].apply(lambda x: x.replace(" ", "") if isinstance(x, str) else "")
dat2["description"] = dat2["description"].apply(lambda x: x.replace(" ", ",") if isinstance(x, str) else "")
dat2["author"] = dat2["author"].apply(lambda x: x.replace(" ", "") if isinstance(x, str) else "")

# Combine all text into tags
dat2["tags"] = dat2["genre"] + " " + dat2["description"] + " " + dat2["author"]
