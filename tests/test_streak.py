import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Tests that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_longest_streak_wins():
    """Tests that the function correctly identifies the longest of multiple streaks."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_with_zeros_and_negatives():
    """Tests that zeros and negative numbers correctly break streaks."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 5, -5, 1]) == 3

def test_all_positive():
    """Tests a simple case with all positive numbers."""
    assert longest_positive_streak([1, 1, 1]) == 3

def test_no_positive_numbers():
    """Tests a list with no positive numbers."""
    assert longest_positive_streak([-1, -2, -3, 0]) == 0

def test_streak_at_end():
    """Tests when the longest streak is at the end of the list."""
    assert longest_positive_streak([1, -2, 3, 4, 5, 6]) == 4

def test_streak_at_beginning():
    """Tests when the longest streak is at the beginning of the list."""
    assert longest_positive_streak([1, 2, 3, 4, -5, 6]) == 4

def test_single_element_list():
    """Tests lists with a single element."""
    assert longest_positive_streak([5]) == 1
    assert longest_positive_streak([-5]) == 0
    assert longest_positive_streak([0]) == 0