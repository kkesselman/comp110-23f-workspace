"""Combining two lists into a dictionary."""


__author__ = 730395385 


def zip(keys: list[str], values: list[int]) -> dict[str, int]:
    """Defining zip function to be lists at each index."""
    if len(keys) != len(values):
        return dict()
    if keys == list() or values == list():
        return dict()
    zipper: dict[str, int] = {}
    x: int = 0
    while x < len(keys):
        zipper[keys[x]] = values[x]
        x += 1
    return zipper