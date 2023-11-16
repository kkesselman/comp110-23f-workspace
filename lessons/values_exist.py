def value_exists(dict_input: dict[str, int], value_input: int) -> bool: 
    """Returns if value is in dictionary."""
    for key in dict_input: 
        if value_input == dict_input[key]: 
            return True 
    return False 
        
print(value_exists({"a": 2 , "b": 4 , "c": 7 , "d": 1}, 5))