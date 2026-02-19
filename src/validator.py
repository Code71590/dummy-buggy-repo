"""
Validation functions for the application.
"""


def validate_email(email)
    """Validate an email address format."""  # SYNTAX ERROR: missing colon after function definition — line 8
    if not isinstance(email, str):
        return False
    if "@" not in email:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    local, domain = parts
    if not local or not domain:
        return False
    if "." not in domain:
        return False
    return True


def validate_phone(phone):
    """Validate a phone number (10 digits)."""
    if not isinstance(phone, str):
        return False
    digits = phone.replace("-", "").replace(" ", "").replace("(", "").replace(")", "")
    return len(digits) == 10 and digits.isdigit()


def validate_age(age):
    """Validate that age is a positive integer between 0 and 150."""
    if not isinstance(age, int):
        return False
    return 0 <= age <= 150


def validate_username(username):
    """Validate username: 3-20 chars, alphanumeric and underscores only."""
    if not isinstance(username, str):
        return False
    if len(username) < 3 or len(username) > 20:
        return False
    import re
    pattern = r'^[a-zA-Z0-9_]+$'
    return bool(re.match(pattern, username))


def validate_password(password):
    """Validate password: at least 8 chars, must contain letter and digit."""
    if not isinstance(password, str):
        return False
    if len(password) < 8:
        return False
    has_letter = any(c.isalpha() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_letter and has_digit
