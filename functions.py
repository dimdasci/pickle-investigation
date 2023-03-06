"""Provides functions to modify object's behavior"""

def function_a(value: int) -> int:
    """Checks if value is between 1 and 3 incluseve"""
    print(f"Function A({value})")
    return max(1, min(value, 3))

def function_b(text: str, repeats: int) -> list[str]:
    """Repeats text repeats times and splits it by whitespace"""
    print(f"Function B('{text}', {repeats})")

    adjusted_repeats = function_a(repeats)
    return text.split() * adjusted_repeats
