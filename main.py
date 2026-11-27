import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

documents = {
    "Document 1": "Python is a popular programming language.",
    "Document 2": "Machine learning is a part of artificial intelligence.",
    "Document 3": "Python is used in artificial intelligence.",
    "Document 4": "Deep learning is a type of machine learning.",
    "Document 5": "Natural language processing helps computers understand text."
}

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

# Text preprocessing
def preprocess(text):
    words = word_tokenize(text.lower())

    processed_words = [
        stemmer.stem(word)
        for word in words
        if word.isalpha() and word not in stop_words
    ]

    return processed_words

# Process documents
processed_docs = {}

for name, text in documents.items():
    processed_docs[name] = preprocess(text)

# Search function
def search_engine(query):

    query_words = preprocess(query)
    results = {}

    for name, words in processed_docs.items():

        score = sum(
            1 for word in query_words
            if word in words
        )

        if score > 0:
            results[name] = score

    return sorted(
        results.items(),
        key=lambda x: x[1],
        reverse=True
    )

# Main program
print("================================")
print("       MINI SEARCH ENGINE")
print("================================")

while True:

    query = input("\nEnter search query (or type exit): ")

    if query.lower() == "exit":
        print("Thank you for using Mini Search Engine!")
        break

    results = search_engine(query)

    if results:
        print("\nSearch Results:")

        for name, score in results:
            print("\n", name)
            print("Score:", score)
            print("Content:", documents[name])

    else:
        print("No relevant documents found.")
