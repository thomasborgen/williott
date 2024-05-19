from fastapi import Depends
from hypermedia import Button, Div, Header2
from hypermedia.models import ElementList, Element

from williott.pokedex.dependencies import get_pokemon_ids_by_generation
from williott.pokedex.views.base import base
from williott.pokedex.views.common import render_pokemon_fab


def render_generations_partial(
    pokemon_ids: list[int] = Depends(get_pokemon_ids_by_generation),
):
    generations = [
        Button(
            text=str(gen),
            hx_get=f"/pokedex/generations/{gen}",
            hx_target="#content",
            hx_swap="innerHTML",
            hx_push_url="true",
        )
        for gen in range(1, 10)
    ]

    pokemon = [render_pokemon_fab(id) for id in pokemon_ids]

    return ElementList(
        Div(
            Div(
                Header2(classes=["text_center"], text="PokeDex"),
                classes=["stack vertical center_items"],
            ),
            Div(
                *generations,
                classes=[
                    "stack auto_size_flex_items spacing_small horizontal center_items"
                ],
            ),
            Div(
                *pokemon,
                id="pokemon_list",
                classes=["stack horizontal wrap spacing_small space_between"],
            ),
            classes=["stack vertical spacing_medium"],
        ),
    )


def render_generations(
    partial: Element = Depends(render_generations_partial),
):
    return base().extend("content", partial)
