import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import random

positive_reviews = [
    "Amazing movie", "Loved the acting", "Fantastic storyline", "Great direction", "Best film ever",
    "Wonderful experience", "Highly recommend", "Brilliant performance", "Heartwarming plot", "A must-watch",
    "Stellar visuals", "Superb soundtrack", "Top-notch", "Mind-blowing scenes", "Very touching",
    "Great character development", "Loved the climax", "Worth watching", "Entertaining and fun", "Awesome!",
    "Great casting", "Emotionally powerful", "Inspiring", "Beautiful film", "Impressive work",
    "Masterpiece", "Well directed", "Best acting", "Enjoyed it a lot", "Perfect!",
    "Flawless", "Captivating", "Clever writing", "Strong characters", "Fun and fast-paced",
    "Pleasantly surprised", "Exceeded expectations", "Well shot", "Vivid storytelling", "Great cinematography",
    "Emotional", "Loved every scene", "Wonderful journey", "Realistic and touching", "Charming",
    "Super engaging", "Best movie this year", "Artistic", "Very well made", "Solid entertainment"
]

negative_reviews = [
    "Terrible movie", "Horrible acting", "Boring plot", "Worst film ever", "Do not recommend",
    "Disappointing", "Waste of time", "Poor direction", "Bad script", "Awful experience",
    "Slow and dull", "Lackluster", "Too predictable", "Uninteresting", "No chemistry",
    "Weak characters", "Flat storyline", "Bad cinematography", "Overacted", "Unbearable",
    "Cringeworthy", "Painfully slow", "Mediocre", "Low quality", "Forgettable",
    "Unrealistic", "Poor dialogue", "Missed potential", "Unsatisfying", "Too long",
    "Unwatchable", "Lame", "Bad editing", "Zero depth", "Didn't enjoy",
    "Clumsy", "Overrated", "Tiresome", "Monotonous", "Frustrating",
    "Too loud", "Not engaging", "Cheap effects", "Badly written", "Dumb plot",
    "Disjointed", "Confusing", "Hard to follow", "Lacked emotion", "Failed to deliver"
]

reviews = positive_reviews + negative_reviews
sentiments = ['positive'] * 50 + ['negative'] * 50
combined = list(zip(reviews, sentiments))
random.shuffle(combined)

df = pd.DataFrame(combined, columns=["Review", "Sentiment"])

vectorizer = CountVectorizer(stop_words='english', max_features=500)
X = vectorizer.fit_transform(df['Review'])
y = df['Sentiment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy on test set: {accuracy:.2f}")

def predict_review_sentiment(model, vectorizer, review):
    vectorized = vectorizer.transform([review])
    prediction = model.predict(vectorized)[0]
    return prediction

print(predict_review_sentiment(model, vectorizer, "This movie was amazing and fun"))
print(predict_review_sentiment(model, vectorizer, "It was a boring and dull film"))
