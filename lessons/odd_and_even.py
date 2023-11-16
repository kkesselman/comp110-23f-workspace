"""Return list of elements that are odd with an even index."""

def odd_and_even(input: list[int]) -> list[int]: 
    """Returns odd numbers with even indexes."""
    output: list[int] = list()
    idx: int = 0 
    while idx < len(input): 
        if idx % 2 == 0 and input[idx] % 2 != 0: 
            output.append(input[idx])
        idx += 1 
    return output 