from fastapi import Path
from fastapi import Depends

from typing import Any

from sqlmodel import Session

from williott.dependencies import get_session
from williott.pokemon.models import Species, Pokemon


def get_species(
    session: Session = Depends(get_session), pokemon_id: int = Path(...)
) -> Species:
    species = session.get(Species, pokemon_id)

    if not species:
        raise ValueError(f"Pokemon {pokemon_id} not found")

    return species
