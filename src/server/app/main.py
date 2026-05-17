import sys
import os
from fastapi import FastAPI

# Because `fastapi dev` cannot find modules in steamWS
# ---
current_dir: str = os.path.dirname(os.path.abspath(__file__))
submodule_path: str = os.path.join(current_dir, "steamWS", "src")

if submodule_path not in sys.path:
    sys.path.insert(0, submodule_path)
# ---

from app.steamWS.src.search.search import get_data_from_id, get_id_from_name
from app.steamWS.src.utils.utils import GameData

app = FastAPI()


@app.get("/")
def read_root():
    return "Search for a game's data in /games/{name}"


@app.get("/games/{name}")
def read_game(name: str):
    id: str = get_id_from_name(name)
    data: GameData = get_data_from_id(id)
    return {"data": data}
