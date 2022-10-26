"""EX05 - `list` Utility Functions - TESTS."""
__author__ = "730566062"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_one_even() -> None:
    """Tests for evens when there is only one even number."""
    assert only_evens([1, 2, 3]) == [2]


def test_only_evens_no_even() -> None:
    """Tests for evens when there is no even numbers."""
    assert only_evens([1, 5, 3]) == []


def test_only_evens_all_even() -> None:
    """Tests for evens when all of the numbers are even numbers."""
    assert only_evens([4, 4, 4]) == [4, 4, 4]


def test_sub_start_idx_0() -> None:
    """Tests for when start index is zero."""
    a_list = [10, 20, 30, 40]
    assert sub(a_list, 0, 3) == [10, 20, 30]


def test_sub_start_idx_neg() -> None:
    """Tests for when start index is negative."""
    a_list = [10, 20, 30, 40]
    assert sub(a_list, -1, 3) == [10, 20, 30]


def test_sub_end_idx_greater() -> None:
    """Tests for when end index is greater than the length of the list."""
    a_list = [10, 20, 30, 40]
    assert sub(a_list, -1, 6) == [20, 30, 40]


def test_concat_list_diff_lengths() -> None:
    """Tests for when the lists are differing lengths."""
    assert concat([1, 2, 3], [4, 4, 4, 4]) == [1, 2, 3, 4, 4, 4, 4]


def test_concat_identical_lists() -> None:
    """Tests for when the lists are identical."""
    assert concat([1, 2, 3], [1, 2, 3]) == [1, 2, 3, 1, 2, 3]


def test_concat_empty_lists() -> None:
    """Tests for when the lists are empty."""
    assert concat([], []) == []