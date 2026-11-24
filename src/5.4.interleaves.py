"""Interleave elements from multiple iterables."""

from collections.abc import Iterable


def interleave(*args: Iterable) -> list:
    """Return elements from multiple iterables in interleaved order."""
    
    result = []

    for group in zip(*args):
        result.extend(group)

    return result


if __name__ == "__main__":
    print(interleave("abc", [1, 2, 3], ("!", "@", "#")))
