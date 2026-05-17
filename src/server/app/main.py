import sys
from fastapi import FastAPI
from pathlib import Path

# Because `fastapi dev` cannot find modules in steamWS
# ---
src_dir: Path = Path(__file__).resolve().parent.parent.parent
submodule_root: Path = src_dir
# For the submodule to work within itself
submodule_path: Path = src_dir / "steamWS" / "src"

if str(submodule_root) not in sys.path:
    sys.path.insert(0, str(submodule_root))

if str(submodule_path) not in sys.path:
    sys.path.insert(0, str(submodule_path))
# ---

from steamWS.src.search.search import get_data_from_id, get_id_from_name
from steamWS.src.utils.utils import GameData

app = FastAPI()


@app.get("/")
def read_root():
    return "Search for a game's data in /games/{name}"


@app.get("/games/{name}")
def read_game(name: str):
    id: str = get_id_from_name(name)
    data: GameData = get_data_from_id(id)
    return {"data": data}
