import json

database = {}

with open("williott/pokemon_db/pokedex.json") as f:
    print("read")
    database = json.load(f)
