from fastapi import Depends
from hypermedia import Button, Div, Header2
from hypermedia.models import Element

from williott.pokedex.views.base import base
from williott.pokedex.views.common import render_pokemon_fab
from williott.pokemon.dependencies import get_generation
from williott.pokemon.models import GenerationRead


def render_generations_partial(
    generation: GenerationRead = Depends(get_generation),
):
    generations = [
        Button(
            text=str(gen),
            hx_get=f"/pokedex/generations/{gen}",
            hx_target="#content",
            hx_swap="innerHTML",
        )
        for gen in range(1, 10)
    ]

    pokemon = [render_pokemon_fab(species.id) for species in generation.species]

    # pokemon = [render_pokemon_fab(id) for id in range(1, 151)]

    return Div(
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
    )


def render_generations(
    partial: Element = Depends(render_generations_partial),
):
    return base().extend("content", partial)
