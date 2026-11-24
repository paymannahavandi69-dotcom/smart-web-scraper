import json
import csv


def save_to_json(data: list, filepath: str) -> None:
    """Save a list of dicts or strings to a JSON file."""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(data)} items to {filepath}")


def save_to_csv(data: list[dict], filepath: str, fieldnames: list[str]) -> None:
    """Save a list of dicts to a CSV file."""
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"Saved {len(data)} items to {filepath}")