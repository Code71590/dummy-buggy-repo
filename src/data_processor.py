"""
Data processing module with various operations.
"""
import json
import csv
from typing import List, Dict, Any
import numpy  # IMPORT ERROR: numpy not in requirements, will cause ImportError


def process_data(data: List[Dict]) -> List[Dict]:
    """Process a list of records."""
    result = []
    for item in data:
        processed = {
            "id": item.get("id"),
            "name": item.get("name", "").strip(),
            "value": item.get("value", 0),
        }
        result.append(processed)
    return result


def filter_by_value(data: List[Dict], threshold: int) -> List[Dict]:
    """Filter records where value is above threshold."""
    # LOGIC ERROR: should be > threshold, not < threshold
    return [item for item in data if item.get("value", 0) < threshold]


def compute_statistics(values: List[float]) -> Dict[str, float]:
    """Compute basic statistics for a list of values."""
    if not values:
        return {}
    n = len(values)
    mean = sum(values) / n
    variance = sum((x - mean) ** 2 for x in values) / n
    std_dev = variance ** 0.5
    return {
        "mean": mean,
        "std_dev": std_dev,
        "min": min(values),
        "max": max(values),
        "count": n,
    }


def load_json_file(filepath: str) -> Any:
    """Load JSON from a file."""
    with open(filepath, "r") as f:
        return json.load(f)


def save_json_file(filepath: str, data: Any) -> None:
    """Save data to a JSON file."""
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)


def read_csv(filepath: str) -> List[Dict]:
    """Read a CSV file and return list of dicts."""
    rows = []
    with open(filepath, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(dict(row))
    return rows


def flatten_list(nested: List) -> List:
    """Flatten a nested list one level deep."""
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(item)
        else:
            flat.append(item)
    return flat


def group_by_key(data: List[Dict], key: str) -> Dict[str, List]:
    """Group a list of dicts by a given key."""
    groups = {}
    for item in data:
        k = item.get(key, "unknown")
        if k not in groups:
            groups[k] = []
        groups[k].append(item)
    return groups
