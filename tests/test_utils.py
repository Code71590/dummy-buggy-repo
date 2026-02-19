"""
Tests for utils.py
"""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from utils import (
    add_numbers,
    multiply_numbers,
    calculate_average,
    find_max,
    find_min,
    is_palindrome,
    factorial,
    count_words,
    reverse_string,
    is_even,
    square,
)


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0


def test_multiply_numbers():
    assert multiply_numbers(3, 4) == 12
    assert multiply_numbers(0, 5) == 0
    assert multiply_numbers(-2, 3) == -6


def test_calculate_average():
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0
    assert calculate_average([]) == 0
    assert calculate_average([10]) == 10.0


def test_find_max():
    assert find_max([1, 5, 3, 2, 4]) == 5
    assert find_max([]) is None
    assert find_max([-1, -5, -3]) == -1


def test_find_min():
    assert find_min([1, 5, 3, 2, 4]) == 1
    assert find_min([]) is None
    assert find_min([-1, -5, -3]) == -5


def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("A man a plan a canal Panama") is True


def test_factorial():
    # This test will FAIL because of the logic bug in factorial()
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1  # Bug: factorial(1) loops infinitely due to logic error


def test_count_words():
    assert count_words("hello world") == 2
    assert count_words("") == 0
    assert count_words("one") == 1


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"


def test_is_even():
    assert is_even(4) is True
    assert is_even(3) is False
    assert is_even(0) is True


def test_square():
    assert square(3) == 9
    assert square(0) == 0
    assert square(-2) == 4
