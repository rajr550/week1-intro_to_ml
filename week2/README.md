
# Assignment 2.1: Text Vectorization Implementation

## Objective
To manually implement the TF-IDF algorithm and compare its results with scikit-learn's CountVectorizer and TfidfVectorizer using a small sample corpus.


### Manual TF-IDF
- **Tokenization:** Used NLTK's `word_tokenize()` for accurate splitting of text into words.
- **TF Calculation:** Term Frequency = (word count in doc) / (total words in doc).
- **IDF Calculation:** IDF = log(N / (1 + df)) + 1, with smoothing to avoid division by zero.
- **TF-IDF:** Product of TF and IDF for each word in a document.

### CountVectorizer
- Converts each document into a vector of raw word counts.

### TfidfVectorizer
- Built-in TF-IDF implementation from scikit-learn.
- Applies L2 normalization and uses log-based IDF with smoothing.

## Observations

### Comparison of Scores
- **Manual TF-IDF** gives similar trends to scikit-learn's TfidfVectorizer, though numerical values may differ slightly due to normalization.
- **CountVectorizer** reflects only frequency, making it less meaningful for identifying important terms.

### Common Word Analysis
- Words like **"the"** appear in all documents, resulting in a **low IDF** score.
- In **TF-IDF**, such words have reduced importance.
- In **CountVectorizer**, frequent words still get high scores regardless of relevance.

## Conclusion
Manual implementation clarifies the inner workings of TF-IDF. While scikit-learn provides optimized solutions, understanding the manual steps helps in customizing and debugging text analysis workflows.

## Files Included
- `assignment_2_1_tfidf_nltk.ipynb`: Jupyter notebook with all code and output.
- `Readme.md`: This summary.
