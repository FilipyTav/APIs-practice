import json
import requests

BASE_URL: str = "http://127.0.0.1:8000"
game_name: str = "elden ring"


def fetch_game(name: str) -> str:
    try:
        response: requests.Response = requests.get(f"{BASE_URL}/games/{name}")

        if response.status_code == 200:
            data: str = response.json()
            return json.dumps(data, indent=4)
        else:
            print(f"Failed with status code: {response.status_code}")
            print(f"Details: {response.text}")

    except:
        print("Error: Could not get response from server.")

    return ""


game_data: str = fetch_game(game_name)
if game_data:
    print("------------------------")
    print(game_data)
    print("------------------------")
