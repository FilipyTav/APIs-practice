import json
from typing import Any
import requests

BASE_URL: str = "http://127.0.0.1:8000"
game_name: str = "elden ring"


def fetch_game(name: str) -> dict[Any, str]:
    try:
        response: requests.Response = requests.get(f"{BASE_URL}/games/{name}")

        if response.status_code == 200:
            data: dict[Any, str] = response.json()
            return data
        else:
            print(f"Failed with status code: {response.status_code}")
            print(f"Details: {response.text}")

    except:
        print("Error: Could not get response from server.")

    return {}


game_data: dict[Any, str] = fetch_game(game_name)
if game_data:
    print("------------------------")
    print(json.dumps(game_data, indent=4))
    print("------------------------")
