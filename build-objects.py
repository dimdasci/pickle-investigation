import pickle
from vectorizer import Vectoriser
from wrapped_vectorizer import WrappedVectorizer

def function_a(value: int) -> int:
    """Checks if value is between 1 and 3 incluseve"""
    print(f"Function A({value})")
    return max(1, min(value, 3))

def function_b(text: str, repeats: int) -> list[str]:
    """Repeats text repeats times and splits it by whitespace"""
    print(f"Function B('{text}', {repeats})")

    adjusted_repeats = function_a(repeats)
    return text.split() * adjusted_repeats


def main():
    vectorizer = Vectoriser(repeats=2, transform_fn=function_b)
    w_vectorizer = WrappedVectorizer(repeats=5)

    text = "one two"

    result = vectorizer.transform(text=text)
    print("vectoriser:\n", result)

    result = w_vectorizer.transform(text=text)
    print("wrapped vectoriser:\n", result)

    with open("vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)

    with open("wrapped_vectorizer.pkl", "wb") as f:
        pickle.dump(w_vectorizer, f)

if __name__ == "__main__":
    main()
