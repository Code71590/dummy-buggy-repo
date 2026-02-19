"""
Tests for data_processor.py
Note: This will fail with ImportError because data_processor.py imports numpy which is not installed.
"""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

# This import will raise ImportError due to numpy not being available
from data_processor import (
    process_data,
    filter_by_value,
    compute_statistics,
    flatten_list,
    group_by_key,
)


def test_process_data():
    data = [
        {"id": 1, "name": "  Alice  ", "value": 10},
        {"id": 2, "name": "Bob", "value": 20},
    ]
    result = process_data(data)
    assert result[0]["name"] == "Alice"
    assert result[1]["value"] == 20


def test_filter_by_value():
    data = [
        {"id": 1, "value": 5},
        {"id": 2, "value": 15},
        {"id": 3, "value": 25},
    ]
    # Should return items WITH value > 10, but due to bug returns items WITH value < 10
    result = filter_by_value(data, threshold=10)
    assert len(result) == 2  # Expects 2 (items with value 15, 25), will fail due to logic bug
    assert result[0]["value"] == 15


def test_compute_statistics():
    values = [1.0, 2.0, 3.0, 4.0, 5.0]
    stats = compute_statistics(values)
    assert stats["mean"] == 3.0
    assert stats["min"] == 1.0
    assert stats["max"] == 5.0
    assert stats["count"] == 5


def test_compute_statistics_empty():
    result = compute_statistics([])
    assert result == {}


def test_flatten_list():
    nested = [[1, 2], [3, 4], 5]
    result = flatten_list(nested)
    assert result == [1, 2, 3, 4, 5]


def test_group_by_key():
    data = [
        {"category": "A", "value": 1},
        {"category": "B", "value": 2},
        {"category": "A", "value": 3},
    ]
    result = group_by_key(data, "category")
    assert len(result["A"]) == 2
    assert len(result["B"]) == 1
