import pickle
from vectorizer import Vectoriser
from wrapped_vectorizer import WrappedVectorizer

def get_vectorizer(filename: str) -> Vectoriser:
    vectorizer = None
    try:
        with open(filename, "rb") as f:
            vectorizer = pickle.load(f)

    except FileNotFoundError:
        print(f"File {filename} not found.  Aborting")
    
    except AttributeError as e:
        print(f"Unknown attribute {e}")
    
    return vectorizer

def main():
    vectorizer = get_vectorizer("vectorizer.pkl")
    w_vectorizer = get_vectorizer("wrapped_vectorizer.pkl")
    text = "cats are amazing"

    if vectorizer is not None:
        result = vectorizer.transform(text=text)
        print("vectorizer:\n", result)

    if w_vectorizer is not None:
        result = w_vectorizer.transform(text=text)
        print("wrapped vectorizer:\n", result)

if __name__ == "__main__":
    main()
