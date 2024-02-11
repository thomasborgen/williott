# script to index the data.


import json

with open("./williott/pokemon_db/pokedex_input.json") as f:
    data = json.load(f)


new_data = {}

for pokemon in data:
    new_data[pokemon["id"]] = pokemon


with open("./williott/pokemon_db/pokedex.json", "w") as w:
    w.write(json.dumps(new_data))
