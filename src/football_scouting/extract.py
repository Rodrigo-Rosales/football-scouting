import json
from pathlib import Path

import requests

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = PROJECT_ROOT / "data" / "raw"
BASE_URL = "https://raw.githubusercontent.com/hudl/open-data/refs/heads/master/data"


def download_matches(competition_id: int, season_id: int) -> Path:
    """Download a competition's match list from StatsBomb open data, unchanged.

    Args:
        competition_id: StatsBomb competition id (43 is the FIFA World Cup).
        season_id: StatsBomb season id (106 is 2022).

    Returns:
        The path of the saved JSON file in data/raw/.

    Raises:
        requests.HTTPError: If the download fails.
    """
    url = f"{BASE_URL}/matches/{competition_id}/{season_id}.json"

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    RAW_DIR.mkdir(parents=True, exist_ok=True)

    file_path = RAW_DIR / f"matches_{competition_id}_{season_id}.json"
    file_path.write_text(response.text, encoding="utf-8")

    return file_path

def download_events(match_id: int) -> Path:
    """Download a match events gitfrom StatBombs, unchanged.

    Args:
        match_id: Statbombs match id.

    Returns:
        The path of the saved JSON file in data/raw/events/.

    Raises:
        requests.HTTPError: If the download fails.
    """

    url = f"{BASE_URL}/events/{match_id}.json"

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    file_path = RAW_DIR / "events"/ f"match_{match_id}.json"
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(response.text, encoding="utf-8")
    
    return file_path


if __name__ == "__main__":
    path = download_matches(43, 106)
    print(path)

    matches = json.loads(path.read_text(encoding="utf-8"))
    print(f"Total Matches {len(matches)}")

    path = download_events(3857276) 
    print(path)

    events = json.loads(path.read_text(encoding="utf-8"))
    print(f"Total events: {len(events)}")
