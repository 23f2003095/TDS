"""
Tests for the longest_positive_streak function.
"""
import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test with an empty list."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    """Test with multiple streaks to ensure the longest is chosen."""
    assert longest_positive_streak([1, 2, 0, 1, 2, 3, 0, 1]) == 3
    assert longest_positive_streak([1, 2, 3, 4, 0, 1, 2]) == 4

def test_with_zeros_and_negatives():
    """Test with a mix of positive, zero, and negative numbers."""
    assert longest_positive_streak([1, -2, 3, 4, 0, 5]) == 2
    assert longest_positive_streak([-1, -5, 0, -2]) == 0

def test_single_element_inputs():
    """Test with single-element lists."""
    assert longest_positive_streak([1]) == 1
    assert longest_positive_streak([-1]) == 0
    assert longest_positive_streak([0]) == 0

def test_all_positive_inputs():
    """Test with a list of all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_no_positive_streak():
    """Test with lists that should result in a streak of 0."""
    assert longest_positive_streak([-1, -2, -3]) == 0
    assert longest_positive_streak([0, 0, 0]) == 0

def test_streak_at_end():
    """Test when the longest streak is at the end of the list."""
    assert longest_positive_streak([1, 0, 2, 3, 4]) == 3

def test_streak_at_beginning():
    """Test when the longest streak is at the beginning of the list."""
    assert longest_positive_streak([1, 2, 3, 0, 1]) == 3