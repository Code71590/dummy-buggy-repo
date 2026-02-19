"""
Tests for formatter.py
"""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from formatter import (
    format_name,
    format_currency,
    format_percentage,
    truncate_string,
    pad_string,
    snake_to_camel,
    camel_to_snake,
)


def test_format_name():
    assert format_name("John", "Doe") == "John Doe"
    assert format_name("Alice", "Smith") == "Alice Smith"
    # Note: format_name has 2-space indentation (detected by flake8 E111),
    # but the function still runs correctly — it's a style/linting bug, not a runtime bug.


def test_format_currency():
    assert format_currency(1000.5) == "USD 1,000.50"
    assert format_currency(0) == "USD 0.00"
    assert format_currency(1234567.89, "EUR") == "EUR 1,234,567.89"


def test_format_currency_type_error():
    with pytest.raises(TypeError):
        format_currency("not a number")


def test_format_percentage():
    assert format_percentage(0.5) == "50.00%"
    assert format_percentage(1.0) == "100.00%"
    assert format_percentage(0.1234, 1) == "12.3%"


def test_truncate_string():
    assert truncate_string("Hello, World!", 10) == "Hello, ..."
    assert truncate_string("Hi", 10) == "Hi"
    assert truncate_string("Short", 5) == "Short"


def test_truncate_string_type_error():
    with pytest.raises(TypeError):
        truncate_string(123, 5)


def test_pad_string():
    assert pad_string("hello", 10) == "hello     "
    assert pad_string("hello", 10, align="right") == "     hello"
    assert pad_string("hello", 10, align="center") == "  hello   "


def test_pad_string_invalid_align():
    with pytest.raises(ValueError):
        pad_string("hello", 10, align="diagonal")


def test_snake_to_camel():
    assert snake_to_camel("hello_world") == "helloWorld"
    assert snake_to_camel("my_variable_name") == "myVariableName"
    assert snake_to_camel("simple") == "simple"


def test_camel_to_snake():
    assert camel_to_snake("helloWorld") == "hello_world"
    assert camel_to_snake("myVariableName") == "my_variable_name"
    assert camel_to_snake("simple") == "simple"
