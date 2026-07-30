import json
from pathlib import path

CONFIG_FILE = Path(__file__).parent/"settings.json"

with open(CONFIG_FILE,"r") as file:
    settings =json.load(file)

BASE_URL = settings["base_url"]
BROWSER = settings["browser"]
IMPLICIT_WAITS = settings["implicit_wait"]
EXPLICIT_WAITS = settings["explicit_wait"]

