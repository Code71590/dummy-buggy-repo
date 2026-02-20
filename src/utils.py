"""
Utility functions for the application.
"""

import datetime


def add_numbers(a, b):
    """Add two numbers together."""
    return a + b


def multiply_numbers(a, b):
    """Multiply two numbers."""
    return a * b


def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    return total / len(numbers)


def find_max(numbers):
    """Find the maximum value in a list."""
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val


def find_min(numbers):
    """Find the minimum value in a list."""
    if not numbers:
        return None
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val


def is_palindrome(s):
    """Check if a string is a palindrome."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]


def factorial(n):
    """Calculate the factorial of a number."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def get_formatted_date():
    """Get the current date formatted as YYYY-MM-DD."""
    today = datetime.date.today()
    return str(today)


def count_words(text):
    """Count words in a string."""
    if not text:
        return 0
    words = text.split()
    return len(words)


def reverse_string(s):
    """Reverse a string."""
    return s[::-1]


def is_even(n):
    """Check if a number is even."""
    return n % 2 == 0


def square(n):
    """Return the square of a number."""
    return n * n
