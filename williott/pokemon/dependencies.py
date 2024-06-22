from fastapi import Path
from fastapi import Depends

from sqlmodel import Session, col, select

from williott.dependencies import get_session
from williott.pokemon.models import Generation, GenerationRead, Species, SpeciesRead


def get_generation(
    session: Session = Depends(get_session),
    generation_id: int = Path(...),
) -> GenerationRead:
    generation = session.get(Generation, generation_id)

    if not generation:
        raise ValueError(f"Generation {generation_id} not found")

    return GenerationRead.model_validate(generation)


def get_species(
    session: Session = Depends(get_session),
    pokemon_id: int = Path(...),
) -> Species:
    species = session.get(Species, pokemon_id)

    if not species:
        raise ValueError(f"Pokemon {pokemon_id} not found")

    return species


def get_evolutions(
    session: Session = Depends(get_session), species: Species = Depends(get_species)
) -> list[SpeciesRead]:
    statement = (
        select(Species)
        .where(Species.evolution_chain_id == species.evolution_chain_id)
        .order_by(col(Species.order))
    )

    return [
        SpeciesRead.model_validate(species) for species in session.exec(statement).all()
    ]
