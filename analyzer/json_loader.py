import json
from pathlib import Path


def load_match_data():
    """
    Load the match json file and returns its contents as a Python dictionary.
    """

    json_file = Path(__file__).parent.parent / "data" / "argentina_vs_cape_verde.json"

    with open(json_file, "r", encoding="utf-8") as file:
        return json.load(file)
