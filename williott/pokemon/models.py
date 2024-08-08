from sqlmodel import Field, Relationship, SQLModel


class GenerationBase(SQLModel):
    """Base class Generation class."""

    region_id: int
    identifier: str


class Generation(GenerationBase, table=True):
    """The Database Generation class."""

    id: int | None = Field(default=None, primary_key=True, nullable=False)

    species: list["Species"] = Relationship(back_populates="generation")


class GenerationRead(GenerationBase):
    id: int
    species: list["SpeciesReadOnlyId"]


class GenerationReadWithoutSpecies(GenerationBase):
    id: int


class SpeciesBase(SQLModel):
    """Base class for all pokemon related classes."""

    id: int | None = Field(default=None, primary_key=True, nullable=False)
    identifier: str = Field(sa_column_kwargs={"unique": True})

    generation_id: int = Field(foreign_key="generation.id")
    evolves_from_species_id: int | None
    evolution_chain_id: int | None
    color_id: int | None
    shape_id: int | None
    habitat_id: int | None
    gender_rate: int
    capture_rate: int
    base_happiness: int | None
    is_baby: bool
    hatch_counter: int | None
    has_gender_differences: bool
    growth_rate_id: int | None
    forms_switchable: bool
    is_legendary: bool
    is_mythical: bool
    order: int
    conquest_order: int | None


class Species(SpeciesBase, table=True):
    """The Database Species class."""

    # back populates
    generation: "Generation" = Relationship(back_populates="species")
    pokemon: list["Pokemon"] = Relationship(back_populates="species")
    names: list["SpeciesName"] = Relationship(back_populates="species")
    descriptions: list["Description"] = Relationship(back_populates="species")


class SpeciesRead(SpeciesBase):
    id: int
    generation: "GenerationReadWithoutSpecies"
    pokemon: list["PokemonReadWithoutSpecies"]
    names: list["SpeciesName"]
    descriptions: list["Description"]


class SpeciesReadOnlyId(SpeciesBase):
    id: int


class SpeciesName(SQLModel, table=True):
    """The Database SpeciesNames class."""

    species_id: int = Field(foreign_key="species.id", primary_key=True)
    species: "Species" = Relationship(back_populates="names")
    language_id: int = Field(foreign_key="language.id", primary_key=True)
    language: "Language" = Relationship()
    name: str
    genus: str | None


class Description(SQLModel, table=True):
    """The Database Description class."""

    species_id: int = Field(foreign_key="species.id", primary_key=True)
    species: "Species" = Relationship(back_populates="descriptions")
    version_id: int = Field(primary_key=True)
    language_id: int = Field(foreign_key="language.id", primary_key=True)
    language: "Language" = Relationship(back_populates="descriptions")
    text: str


class Language(SQLModel, table=True):
    """The Database Language class."""

    id: int | None = Field(default=None, primary_key=True, nullable=False)
    iso639: str
    iso3166: str
    identifier: str
    official: bool
    order: int

    species_names: list["SpeciesName"] = Relationship(back_populates="language")
    descriptions: list["Description"] = Relationship(back_populates="language")


class PokemonBase(SQLModel):
    """Base class for all pokemon related classes."""

    id: int | None = Field(default=None, primary_key=True, nullable=False)
    identifier: str = Field(sa_column_kwargs={"unique": True})
    species_id: int = Field(foreign_key="species.id")

    height: int
    weight: int
    base_experience: int | None
    order: int | None
    is_default: bool


class Pokemon(PokemonBase, table=True):
    """The Database Pokemon class."""

    species: "Species" = Relationship(back_populates="pokemon")
    forms: list["Form"] = Relationship(back_populates="pokemon")


class PokemonRead(PokemonBase):
    species: "SpeciesRead"
    forms: list["FormRead"]


class PokemonReadWithoutSpecies(PokemonBase):
    pass


class FormBase(SQLModel):
    """Base class Form class."""

    identifier: str
    form_identifier: str | None
    pokemon_id: int = Field(foreign_key="pokemon.id")
    introduced_in_version_group_id: int
    is_default: bool
    is_battle_only: bool
    is_mega: bool
    form_order: int
    order: int


class Form(FormBase, table=True):
    """The Database Form class."""

    id: int | None = Field(default=None, primary_key=True, nullable=False)
    pokemon: "Pokemon" = Relationship(back_populates="forms")
    names: list["FormName"] = Relationship(back_populates="form")


class FormRead(FormBase):
    id: int
    pokemon: "PokemonRead"


class FormNameBase(SQLModel):
    """Base class Form class."""

    pokemon_form_id: int = Field(foreign_key="form.id")
    language_id: int
    form_name: str | None
    pokemon_name: str | None


class FormName(FormNameBase, table=True):
    """The Database Form class."""

    id: int | None = Field(default=None, primary_key=True, nullable=False)

    form: "Form" = Relationship(back_populates="names")


class FormNameRead(FormNameBase):
    id: int
    form: "Form"
