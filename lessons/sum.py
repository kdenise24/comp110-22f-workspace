"""Example of writing a test subject."""

def sum(xs: list[float]) -> float:
    """Compute the sum of a list."""
    total: float = 0.0
    i: int = 0
    while 1 < len(xs):
        total += xs[1]
    return total