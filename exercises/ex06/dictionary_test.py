"""Testing dictionary functions."""

from __future__ import annotations 

__author__ = 730395385


from exercises.ex06.dictionary import invert 
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count
from exercises.ex06.dictionary import alphabetizer
from exercises.ex06.dictionary import update_attendance


def test_invert_one_pair() -> None: 
    """Testing if invert works with one key-value pair."""
    input: dict[str, str] = {"x": "1"}
    assert invert(input) == {"1": "x"}


def test_invert_two_pairs() -> None: 
    """Testing invert with two key-value pairs."""
    input: dict[str, str] = {"x": "1", "y": "2"} 
    assert invert(input) == {"1": "x", "2": "y"}


def test_invert_empty_list() -> None:
    """Testing invert with an empty list."""
    input: dict[str, str] = {}
    assert invert(input) == dict()


def test_fav_color_purple() -> None: 
    """Testing favorite_color with only purple."""
    color_dict: dict[str, str] = {"Katie": "purple", "Allison": "purple", "Sabrina": "purple"} 
    assert favorite_color(color_dict) == "purple" 


def test_fav_color_unique() -> None: 
    """Testing favorite_color with unique colors."""
    color_dict: dict[str, str] = {"Katie": "red", "Allison": "orange", "Sabrina": "yellow", "Maren": "green", "Josh": "blue", "Kenendy": "purple"}
    assert favorite_color(color_dict) == "red"


def test_fav_color_multiples() -> None: 
    """Testing favorite_color with multiple answers for the same color."""
    color_dict: dict[str, str] = {"Katie": "purple", "Allison": "red", "Sabrina": "purple", "Josh": "blue"} 
    assert favorite_color(color_dict) == "purple"


def test_count_unique() -> None: 
    """Testing count where each value is unique."""
    count_input = ["Katie", "Allison"] 
    assert count(count_input) == {"Katie": 1, "Allison": 1} 


def test_count_multiples() -> None: 
    """Testing count with repeated values."""
    count_input = ["Katie", "Katie", "Allison", "Katie"]
    assert count(count_input) == {"Katie": 3, "Allison": 1} 


def test_count_empty() -> None: 
    """Testing count with empty list."""
    count_input: list[str] = []
    assert count(count_input) == dict() 


def test_alphabetizer_a() -> None: 
    """Testing alphabetizer with words beginning with a."""
    input_list = ["apple", "alphabet", "anger"]
    assert alphabetizer(input_list) == {"a": ["apple", "alphabet", "anger"]}


def test_alphabetizer_abc() -> None: 
    """Testing alphabetizer with words beginning with a, b and c."""
    input_list = ["apple", "ball", "cat", "axe"]
    assert alphabetizer(input_list) == {"a": ["apple", "axe"], "b": ["ball"], "c": ["cat"]} 


def test_alphabetizer_empty_list() -> None: 
    """Testing alphabetizer with an empty list."""
    input_list: list[str] = [] 
    assert alphabetizer(input_list) == dict()


def test_update_attendance_add_one_student() -> None: 
    """Testing update attendance with adding one student."""
    attendance_dict: dict[str, list[str]] = {"Monday": ["Katie", "Allison"]} 
    day: str = "Monday"
    person: str = "Sabrina"
    assert update_attendance(attendance_dict, day, person) == {"Monday": ["Katie", "Allison", "Sabrina"]} 


def test_update_attendance_add_day_existing_student() -> None: 
    """Testing update attendance adding a day of attendance to existing student."""
    attendance_dict: dict[str, list[str]] = {"Monday": ["Katie", "Allison"]}
    day: str = "Tuesday"
    person: str = "Katie"
    assert update_attendance(attendance_dict, day, person) == {"Monday": ["Katie", "Allison"], "Tuesday": ["Katie"]}


def test_update_attendance_empty_log() -> None: 
    """Testing update attendance with multiple changes to students."""
    attendance_log: dict[str, list[str]] = {}
    day: str = "Tuesday"
    person: str = "Vrinda" 
    assert update_attendance(attendance_log, day, person) == {"Tuesday": ["Vrinda"]}