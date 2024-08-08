import csv

from alembic import op
import sqlalchemy as sa

from williott.pokemon.models import (
    Language,
    Species,
    SpeciesName,
    Pokemon,
    Description,
    Generation,
    Form,
    FormName,
)


def data_entry() -> None:
    # Data migrations

    folder = "migration_data/add_pokemon_models"

    generations = []
    with open(f"{folder}/generations.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row = {key: val if val != "" else None for key, val in row.items()}
            generations.append(
                {
                    **row,
                    "region_id": row["main_region_id"],
                }
            )

    languages = []
    with open(f"{folder}/languages.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row = {key: val if val != "" else None for key, val in row.items()}
            languages.append(
                {
                    **row,
                    "official": int(row["official"]),
                }
            )

    all_species = []
    with open(f"{folder}/species.csv") as f:
        reader = csv.DictReader(f, delimiter=",")
        for row in reader:
            row = {key: val if val != "" else None for key, val in row.items()}
            all_species.append(
                {
                    **row,
                    "is_baby": int(row["is_baby"]),
                    "has_gender_differences": int(row["has_gender_differences"]),
                    "forms_switchable": int(row["forms_switchable"]),
                    "is_legendary": int(row["is_legendary"]),
                    "is_mythical": int(row["is_mythical"]),
                }
            )

    descriptions = []
    with open(f"{folder}/descriptions.csv") as f:
        reader = csv.DictReader(f, delimiter=",", quotechar='"')
        for row in reader:
            row = {key: val if val != "" else None for key, val in row.items()}
            descriptions.append(
                {
                    **row,
                    "text": row["flavor_text"],
                }
            )

    all_pokemon = []
    with open(f"{folder}/pokemon.csv") as f:
        reader = csv.DictReader(f, delimiter=",")
        for row in reader:
            row = {key: val if val != "" else None for key, val in row.items()}
            all_pokemon.append(
                {
                    **row,
                    "is_default": int(row["is_default"]),
                }
            )

    species_names = []
    with open(f"{folder}/species_names.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row = {key: val if val != "" else None for key, val in row.items()}
            species_names.append(
                {
                    **row,
                    "species_id": row["pokemon_species_id"],
                    "language_id": row["local_language_id"],
                }
            )

    forms = []
    with open(f"{folder}/forms.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row = {key: val if val != "" else None for key, val in row.items()}
            forms.append(
                {
                    **row,
                    "is_default": int(row["is_default"]),
                    "is_battle_only": int(row["is_battle_only"]),
                    "is_mega": int(row["is_mega"]),
                }
            )

    form_names = []
    with open(f"{folder}/form_names.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row = {key: val if val != "" else None for key, val in row.items()}
            form_names.append(
                {
                    **row,
                    "form_id": row["pokemon_form_id"],
                    "language_id": row["local_language_id"],
                }
            )

    bind = op.get_bind()
    session = sa.orm.Session(bind=bind)

    session.bulk_insert_mappings(Generation, generations)  # type: ignore
    session.bulk_insert_mappings(Language, languages)  # type: ignore
    session.bulk_insert_mappings(Species, all_species)  # type: ignore
    session.bulk_insert_mappings(Description, descriptions)  # type: ignore
    session.bulk_insert_mappings(Pokemon, all_pokemon)  # type: ignore
    session.bulk_insert_mappings(SpeciesName, species_names)  # type: ignore
    session.bulk_insert_mappings(Form, forms)  # type: ignore
    session.bulk_insert_mappings(FormName, form_names)  # type: ignore

    session.commit()
