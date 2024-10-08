import random
from fastapi import Depends
from hypermedia import Audio, Button, Div, Header1, Header3, Image
from hypermedia.models import Element

import urllib

from williott.pokedex.views.base import base
from williott.pokedex.views.common import (
    render_pokemon_fab_htmx,
    render_species_fab_htmx,
)
from williott.pokemon.dependencies import get_evolutions, get_pokemon, get_species
from williott.pokemon.models import Pokemon, Species, SpeciesRead


image_base_path = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{id}.png"


def render_pokemon_partial(
    evolutions: list[SpeciesRead] = Depends(get_evolutions),
    species: Species = Depends(get_species),
    pokemon: Pokemon = Depends(get_pokemon),
):
    english_name = species.names[8]
    japanese_name = species.names[0]

    english_descriptions = [
        desc for desc in species.descriptions if desc.language_id == 9
    ]

    description = english_descriptions[
        random.randint(0, len(english_descriptions) - 1)
    ].text

    rendered_evolutions = [
        render_species_fab_htmx(species.id, "#content") for species in evolutions
    ]

    names = pokemon.forms[0].names

    form_name_english = english_name.name

    if len(names):
        form_name = [name for name in names if name.language_id == 9][0]

        form_name_english = (
            form_name.pokemon_name or form_name.form_name or form_name_english
        )

    return Div(
        Div(
            Div(
                Image(
                    classes=["pokemon_image"],
                    alt=f"official-artwork of {english_name.name}",
                    src=image_base_path.format(id=pokemon.id),
                ),
                classes=["circle stack horizontal space_evenly"],
            ),
            classes=["stack spacing_small vertical center_items"],
        ),
        Div(
            Header1(english_name.name, id="name_english"),
            Header3(japanese_name.name, id="name_japanese"),
            classes=["stack vertical center_items"],
        ),
        Button(f"#{species.id}", id="number", classes=["pill"]),
        Div(
            Div(
                *rendered_evolutions,
                id="pokemon_list",
                classes=["stack horizontal wrap spacing_small space_evenly"],
            ),
            id="evolution_tree",
            classes=["data_area"],
        ),
        Div(
            description,
            id="description_english",
            classes=["data_area"],
        ),
        Div(
            Div(
                Image(src="/static/loading_pikachu.gif", width="30px"),
                id="spinner",
                classes=["stack horizontal center_items center_content htmx-indicator"],
            ),
            id="cards",
            hx_get=f"/pokedex/cards/{pokemon.id}",
            hx_trigger="load",
            hx_indicator="#spinner",
            classes=["data_area"],
        ),
        Audio(
            id="audio_name_english",
            src=urllib.parse.quote(
                f"/speak/english/This pokemon's name is, {english_name.name}"
            ),
            style="display:none;",
            autoplay=True,
        ),
        Audio(
            id="audio_name_japanese",
            src=urllib.parse.quote(
                f"/speak/japanese/このポケモンの名前は, {japanese_name.name}"
            ),
            preload="none",
            style="display:none;",
        ),
        Audio(
            id="audio_number",
            src=urllib.parse.quote(f"/speak/english/Number, {species.id}"),
            preload="none",
            style="display:none;",
        ),
        Audio(
            id="audio_description_english",
            src=urllib.parse.quote(f"/speak/english/{description}"),
            preload="none",
            style="display:none;",
        ),
        classes=["stack vertical spacing_medium"],
    )


def render_pokemon(
    partial: Element = Depends(render_pokemon_partial),
):
    return base().extend("content", partial)
