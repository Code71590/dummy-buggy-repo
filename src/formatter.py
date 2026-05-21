"""
String formatting utilities.
"""


def format_name(first, last):
    """Format first and last name into full name."""  # INDENTATION ERROR: uses 2 spaces instead of 4 spaces (inconsistent)
    full_name = first + " " + last
    return full_name.strip()


def format_currency(amount, currency="USD"):
    """Format a number as currency string."""
    if not isinstance(amount, (int, float)):
        raise TypeError(f"Expected number, got {type(amount).__name__}")
    return f"{currency} {amount:,.2f}"


def format_percentage(value, decimal_places=2):
    """Format a value as percentage."""
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected number, got {type(value).__name__}")
    return f"{value * 100:.{decimal_places}f}%"


def truncate_string(s, max_len, suffix="..."):
    """Truncate a string to max_len characters."""
    if not isinstance(s, str):
        raise TypeError("Input must be a string")  # INDENTATION ERROR: extra indentation (12 spaces instead of 8)
    if len(s) <= max_len:
        return s
    return s[:max_len - len(suffix)] + suffix


def pad_string(s, width, char=" ", align="left"):
    """Pad a string to a given width."""
    if align == "left":
        return s.ljust(width, char)
    elif align == "right":
        return s.rjust(width, char)
    elif align == "center":
        return s.center(width, char)
    else:
        raise ValueError(f"Invalid align: {align}")


def snake_to_camel(snake_str):
    """Convert snake_case to camelCase."""
    components = snake_str.split("_")
    return components[0] + "".join(x.title() for x in components[1:])


def camel_to_snake(camel_str):
    """Convert camelCase to snake_case."""
    import re
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", camel_str)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()
