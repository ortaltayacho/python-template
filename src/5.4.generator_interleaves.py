"""Interleave elements from multiple iterables using a generator."""

from collections.abc import Iterable, Iterator


def interleave(*args: Iterable) -> Iterator:
    """Yield elements from multiple iterables in interleaved order."""
    for group in zip(*args):
        yield from group


if __name__ == "__main__":
    print(list(interleave('abc', [1, 2, 3], ('!', '@', '#'))))
