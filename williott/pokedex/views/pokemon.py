from fastapi import Depends
from typing import Any
from hypermedia import Audio, Button, Div, Header1, Header3, Image
from hypermedia.models import Element

import urllib

from williott.pokedex.dependencies import pokemon, evolutions
from williott.pokedex.views.base import base
from williott.pokedex.views.common import render_pokemon_fab_htmx


def render_pokemon_partial(
    pokemon: dict[str, Any] = Depends(pokemon),
    evolutions: list[str] = Depends(evolutions),
):
    rendered_evolutions = [
        render_pokemon_fab_htmx(int(id), "#content") for id in evolutions
    ]

    return Div(
        Div(
            Div(
                Image(
                    classes=["pokemon_image"],
                    alt=f"official-artwork of {pokemon['name']['english']}",
                    src=pokemon["image"]["hires"],
                ),
                classes=["circle stack horizontal space_evenly"],
            ),
            classes=["stack spacing_small vertical center_items"],
        ),
        Div(
            Header1(id="name_english", text=pokemon["name"]["english"]),
            Header3(id="name_japanese", text=pokemon["name"]["japanese"]),
            classes=["stack vertical center_items"],
        ),
        Button(id="number", classes=["pill"], text=f"#{pokemon['id']}"),
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
            id="description_english",
            text=pokemon["description"],
            classes=["data_area"],
        ),
        Div(
            Div(
                Image(src="/static/loading_pikachu.gif", width="30px"),
                id="spinner",
                classes=["stack horizontal center_items center_content htmx-indicator"],
            ),
            id="cards",
            hx_get=f"/pokedex/cards/{pokemon['id']}",
            hx_trigger="load",
            hx_indicator="#spinner",
            classes=["data_area"],
        ),
        Audio(
            id="audio_name_english",
            src=urllib.parse.quote(
                f"/speak/english/This pokemon's name is, {pokemon['name']['english']}"
            ),
            style="display:none;",
            autoplay=True,
        ),
        Audio(
            id="audio_name_japanese",
            src=urllib.parse.quote(
                f"/speak/japanese/このポケモンの名前は, {pokemon['name']['japanese']}"
            ),
            style="display:none;",
        ),
        Audio(
            id="audio_number",
            src=urllib.parse.quote(f"/speak/english/Number, {pokemon['id']}"),
            style="display:none;",
        ),
        Audio(
            id="audio_description_english",
            src=urllib.parse.quote(f"/speak/english/{pokemon['description']}"),
            style="display:none;",
        ),
        classes=["stack vertical spacing_medium"],
    )


def render_pokemon(
    partial: Element = Depends(render_pokemon_partial),
):
    return base().extend("content", partial)
