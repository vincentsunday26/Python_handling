#  Task 1: Keyword Highlighter

python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]


# List of keywords to search for
highlighted_keywords = ("good", "excellent", "bad", "poor", "average")
highlighted_reviews = []
for review in python_reviews:
    for keyword in highlighted_keywords:
        review = review.replace(keyword, keyword.upper())
    highlighted_reviews.append(review)

# Print the highlighted reviews
for review in highlighted_reviews:
    print(review)


# Predefined lists of positive and negative words
python_positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

# List of product reviews
python_reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "This was a poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

# Tally positive and negative words in each review
results = []
for review in python_reviews:
    positive_count = sum(review.lower().count(word) for word in python_positive_words)
    negative_count = sum(review.lower().count(word) for word in negative_words)
    results.append((positive_count, negative_count))

# Print the results
for i, (positive_count, negative_count) in enumerate(results):
    print(f"Review {i+1}: {positive_count} positive words, {negative_count} negative words")


def create_summary(review):
    return review[:30] + "…"

# Example usage
review = "This product is really good. I'm impressed with its quality."
summary = create_summary(review)
print(summary)