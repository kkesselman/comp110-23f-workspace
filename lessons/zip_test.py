"""Test my zip function."""


__author__ = 730395385 


from lessons.zip import zip 


def test_zip_one_pair(): 
    """Testing for lists with one item returning dictionary with one key-value pair: use case."""
    test_list_values: list[int] = [4]
    test_list_keys: list[str] = ["Katie"]
    assert zip(test_list_keys, test_list_values) == {"Katie": 4} 


def test_zip_two_pairs(): 
    """Testing for lists with two items returning dictionary with two key-value pairs: use case."""
    test_list_values: list[int] = [4, 5]
    test_list_keys: list[str] = ["Katie", "Kesselman"]
    assert zip(test_list_keys, test_list_values) == {"Katie": 4, "Kesselman": 5} 


def test_zip_edge_case(): 
    """Testing for one empty list returning empty dictionary: edge case."""
    test_list_values: list[int] = []
    test_list_keys: list[str] = ["Katie"]
    assert zip(test_list_keys, test_list_values) == {}