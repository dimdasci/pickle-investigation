class Vectoriser:
    def __init__(self, repeats: int, transform_fn: callable):
        self.repeats = repeats
        self.transform_fn = transform_fn
    
    def transform(self, text: str) -> list[str]:
        return self.transform_fn(text=text, repeats=self.repeats)
