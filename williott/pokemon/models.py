from sqlmodel import Field, Relationship, SQLModel


class SpeciesBase(SQLModel):
    """Base class for all pokemon related classes."""

    id: int | None = Field(default=None, primary_key=True, nullable=False)
    identifier: str = Field(sa_column_kwargs={"unique": True})

    generation_id: int
    evolves_from_species_id: int | None
    evolution_chain_id: int
    color_id: int
    shape_id: int
    habitat_id: int
    gender_rate: int
    capture_rate: int
    base_happiness: int
    is_baby: bool
    hatch_counter: int
    has_gender_differences: bool
    growth_rate_id: int
    forms_switchable: bool
    is_legendary: bool
    is_mythical: bool
    order: int
    conquest_order: int


class Species(SpeciesBase, table=True):
    """The Database Species class."""

    # back populates
    pokemon: list["Pokemon"] = Relationship(back_populates="species")


class PokemonBase(SQLModel):
    """Base class for all pokemon related classes."""

    id: int | None = Field(default=None, primary_key=True, nullable=False)
    identifier: str = Field(sa_column_kwargs={"unique": True})

    height: int
    weight: int
    base_experience: int
    order: int
    is_default: bool


class Pokemon(PokemonBase, table=True):
    """The Database Pokemon class."""

    species_id: int = Field(foreign_key="species.id")
    species: "Species" = Relationship(back_populates="pokemon")
