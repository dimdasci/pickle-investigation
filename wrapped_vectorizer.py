from vectorizer import Vectoriser

class WrappedVectorizer(Vectoriser):

    @staticmethod
    def function_a(value: int) -> int:
        """Checks if value is between 1 and 3 incluseve"""
        print(f"Function A({value})")
        return max(1, min(value, 3))

    @staticmethod
    def function_b(text: str, repeats: int) -> list[str]:
        """Repeats text repeats times and splits it by whitespace"""
        print(f"Function B('{text}', {repeats})")

        adjusted_repeats = WrappedVectorizer.function_a(repeats)
        return text.split() * adjusted_repeats

    def __init__(self, repeats: int):
        super().__init__(repeats=repeats, transform_fn=WrappedVectorizer.function_b)
