from fastapi import Path
from fastapi import Depends

from typing import Any

from williott.pokemon_db.db import database


def get_pokemon_ids_by_generation(
    generation_id: int = Path(...),
) -> list[int]:
    (from_id, to_id) = database["generations"][generation_id]
    return list(range(from_id, to_id + 1))


def pokemon(pokemon_id: int = Path(...)) -> dict[str, Any]:
    return database["pokemon"].get(str(pokemon_id))


def evolutions(pokemon: dict[str, Any] = Depends(pokemon)) -> list[int]:
    hierarchy = []

    if child := pokemon["evolution"].get("prev"):
        if grandchild := database["pokemon"][child[0]]["evolution"].get("prev"):
            hierarchy.append(grandchild[0])
        hierarchy.append(child[0])

    hierarchy.append(pokemon["id"])

    if parents := pokemon["evolution"].get("next"):
        hierarchy.extend(_resolve_parents(parents))

    return hierarchy


def _resolve_parents(parents):
    hierarchy = []

    for parent in parents:
        hierarchy.append(parent[0])
        if grandparents := database["pokemon"][parent[0]]["evolution"].get("next"):
            hierarchy.extend(_resolve_parents(grandparents))

    return hierarchy
