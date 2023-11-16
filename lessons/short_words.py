"""Returns list of words shorter than 5 characters."""

def short_words(input_list: list[str]) -> list[str]: 
    """Returns list of words shorter than 5 characters."""
    output_list: list[str] = list()
    for elem in input_list: 
        if len(elem) < 5: 
            output_list.append(elem)
        else: 
            print(f"{elem} is too long!")
    return output_list

print(short_words(["sun"," cloud","sky"])) 