"""List Utility Functions."""


__author__ = "730395385" 


def all(list_ints: list[int], guess: int) -> bool:
    """Indicate if a guess integer is in a list."""
    if list_ints == list():
        return False 
    else: 
        len_list: int = len(list_ints)
        len_idx: int = 0 
        while len_idx < len_list: 
            if list_ints[len_idx] == guess: 
                len_idx += 1 
            else: 
                return False 
        return True 


def max(input: list[int]) -> int: 
    """Return the maximum value in a list."""
    if len(input) == 0: 
        raise ValueError("max() arg is an empty List")
    else: 
        input_idx: int = 0 
        max_value: int = input[input_idx]
    while input_idx < len(input) - 1: 
        if input[input_idx + 1] > max_value: 
            max_value = input[input_idx + 1]
        input_idx += 1 
    return max_value


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """See if two lists are equal."""
    list1_idx: int = 0 
    list2_idx: int = 0 
    while list1_idx < len(list1) and list2_idx < len(list2): 
        if list1[list1_idx] == list2[list2_idx]: 
            list1_idx += 1
            list2_idx += 1  
        else: 
            return False 
    if list1_idx == len(list1) and list2_idx == len(list2):
        return True
    else:
        return False