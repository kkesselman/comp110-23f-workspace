"""Defining dictionaries."""


__author__ = 730395385 


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Defining a function that inverts the keys and values of a dictionary."""
    inverted_dict: dict[str, str] = {}
    seen_values: list[str] = []
    
    for key in input_dict:
        value = input_dict[key]
        if value in seen_values:
            raise KeyError(f"Duplicate key found: {key}")
        seen_values.append(value)
        inverted_dict[value] = key
    return inverted_dict
    

def favorite_color(color_dict: dict[str, str]) -> str:
    """Returns the most popular color from a dictionary of names and favorite colors."""
    color_count: dict[str, int] = {}
    max_count = 0
    most_popular_color = ""

    for name in color_dict:
        color = color_dict[name]
        if not most_popular_color:
            most_popular_color = color
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

        if color_count[color] > max_count or (color_count[color] == max_count and most_popular_color in color_dict and color_dict[most_popular_color] == color):
            most_popular_color = color
            max_count = color_count[color]

    return most_popular_color


def count(input_list: list[str]) -> dict[str, int]:
    """Counts the frequencies of each value in the input list."""
    result_dict: dict[str, int] = {}

    for item in input_list:
        if item in result_dict:
            result_dict[item] += 1
        else:
            result_dict[item] = 1
    return result_dict


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    """Make lists of works based on the first letter."""
    result_dict: dict[str, list[str]] = {}

    for word in word_list:
        first_letter = word[0].lower() 
        if first_letter.isalpha():
            if first_letter in result_dict:
                result_dict[first_letter].append(word)
            else:
                result_dict[first_letter] = [word]
    return result_dict


def update_attendance(attendance_dict: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Updates the attendance with new information of students."""
    # Check if the day is already a key in the dictionary. 
    if day in attendance_dict:
        # Check if the student is already in the list for a given day. 
        if student not in attendance_dict[day]: 
            attendance_dict[day].append(student)
    else:
        attendance_dict[day] = [student]

    return attendance_dict 