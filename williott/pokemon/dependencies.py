from fastapi import Path
from fastapi import Depends

from sqlmodel import Session, col, select

from williott.dependencies import get_session
from williott.pokemon.models import (
    Generation,
    GenerationRead,
    Pokemon,
    Species,
    SpeciesName,
    SpeciesRead,
)

from sqlalchemy.orm import lazyload


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
    language_id: int = 9,
    species_id: int = Path(...),
) -> Species:
    result = session.get(Species, species_id)

    # statement = (
    # select(Species, SpeciesName).where(Species.id == species_id)
    # .join(SpeciesName, isouter=True)
    # .where(SpeciesName.language_id == language_id)
    # .options(
    #    lazyload(Species..names.and_(SpeciesName.language_id.id == language_id))
    # )
    # )

    # result = session.exec(statement).one_or_none()

    if not result:
        raise ValueError(f"Species {species_id} not found")

    # species, names = result

    # print("TEeeeeeeEEEEST")
    # print(species)

    # print(species.names)
    # print("lelelel")
    # print(names)

    return result


def get_pokemon(
    session: Session = Depends(get_session),
    pokemon_id: int = Path(...),
) -> Pokemon:
    pokemon = session.get(Pokemon, pokemon_id)

    if not pokemon:
        raise ValueError(f"Pokemon {pokemon_id} not found")

    return pokemon


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
