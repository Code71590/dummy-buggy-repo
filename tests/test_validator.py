"""
Tests for validator.py
Note: This file will FAIL to import because validator.py has a SyntaxError.
"""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

# The import below will raise SyntaxError due to missing colon in validator.py
from validator import validate_email, validate_phone, validate_age, validate_username, validate_password


def test_validate_email_valid():
    assert validate_email("user@example.com") is True
    assert validate_email("name.surname@domain.org") is True


def test_validate_email_invalid():
    assert validate_email("not-an-email") is False
    assert validate_email("@nodomain") is False
    assert validate_email("noatsign.com") is False
    assert validate_email(123) is False


def test_validate_phone_valid():
    assert validate_phone("1234567890") is True
    assert validate_phone("123-456-7890") is True


def test_validate_phone_invalid():
    assert validate_phone("123") is False
    assert validate_phone("abcdefghij") is False


def test_validate_age_valid():
    assert validate_age(25) is True
    assert validate_age(0) is True
    assert validate_age(150) is True


def test_validate_age_invalid():
    assert validate_age(-1) is False
    assert validate_age(151) is False
    assert validate_age("25") is False


def test_validate_username_valid():
    assert validate_username("alice123") is True
    assert validate_username("my_user") is True


def test_validate_username_invalid():
    assert validate_username("ab") is False  # too short
    assert validate_username("a" * 21) is False  # too long
    assert validate_username("my-user!") is False  # invalid chars


def test_validate_password_valid():
    assert validate_password("Password1") is True
    assert validate_password("abc12345") is True


def test_validate_password_invalid():
    assert validate_password("short1") is False  # too short
    assert validate_password("alllletters") is False  # no digit
    assert validate_password("12345678") is False  # no letter
