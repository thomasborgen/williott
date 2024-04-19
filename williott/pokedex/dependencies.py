from fastapi import Path


from typing import Annotated

from williott.pokemon_db.db import database


def get_pokemon_ids_by_generation(
    generation_id: int = Path(...),
) -> list[int]:
    print(generation_id)
    (from_id, to_id) = database["generations"][generation_id]
    return list(range(from_id, to_id + 1))


def construct_pokemon(id: int) -> dict[str, int]:
    return {"id": id, "data": database.get(str(id))}
