"""EX07 - Dictionary Functions - TESTS."""
__author__ = "730566062"

from dictionary import invert, favorite_color, count 
import pytest


def test_invert_error() -> None:
    """Tests if the KeyError works."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)
    

def test_invert_long() -> None:
    """Tests for when the dictionary is long."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x', 'e': 'k', 't': 'o'}) == {'z': 'a', 'y': 'b', 'x': 'c', 'k': 'e', 'o': 't'}


def test_invert_short() -> None:
    """Test for with the dictionary is short."""
    assert invert({'apple': 'cat'}) == {'cat': 'apple'}


def test_favorite_color_tie() -> None:
    """Tests for when there is a tie between the colors."""
    assert favorite_color({"Marc": "yellow", "Eric": "yellow", "Ezri": "blue", "Kris": "blue"}) == "yellow"


def test_favorite_color_same() -> None:
    """Tests for when everyone have the same favorite color."""
    assert favorite_color({"Marc": "yellow", "Eric": "yellow", "Ezri": "yellow", "Kris": "yellow"}) == "yellow"


def test_favorite_color_correct() -> None:
    """Tests if favorite color finds the more frequently favorite color."""
    assert favorite_color({"Marc": "yellow", "Eric": "red", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_count_small() -> None:
    """Tests for when the list is small."""
    assert count(['Kaki', 'Kaki', 'Lily', 'Ada', 'Nellie']) == {'Kaki': '2', 'Lily': '1', 'Ada': '1', 'Nellie': '1'}


def test_count_large() -> None:
    """Tests for when the list is large."""
    assert count(['Kaki', 'Kaki', 'Lily', 'Kaki', 'Kaki', 'Lily', 'Ada', 'Nellie', 'Kaki', 'Kaki', 'Lily', 'Ada', 'Nellie', 'Ada', 'Kaki', 'Kaki', 'Lily', 'Ada', 'Nellie', 'Nellie', 'Kaki', 'Kaki', 'Lily', 'Ada', 'Nellie']) == {'Kaki': 10, 'Lily': 5, 'Ada': 5, 'Nellie': 5}