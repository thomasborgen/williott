from fastapi import Depends
from hypermedia import Anchor, Button, Div, Header2, Image
from hypermedia.models import ElementList, Element

from williott.pokedex.dependencies import get_pokemon_ids_by_generation
from williott.pokedex.views.base import base


def render_pokemon_fab(id: int):
    return Anchor(
        Div(
            Image(
                alt=f"pokemon with id: {id}",
                src=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png",
            ),
            classes=["fab_circle"],
        ),
        href=f"/pokedex/pokemon/{id}",
        classes=["fab static_size"],
    )


def render_index_partial(
    pokemon_ids: list[int] = Depends(get_pokemon_ids_by_generation),
):
    generations = [
        Button(
            text=str(gen),
            hx_get=f"/pokedex/{gen}",
            hx_target="#content",
            hx_swap="innerHTML",
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
            classes=["content stack vertical spacing_medium"],
        ),
    )


def render_index(
    partial: Element = Depends(render_index_partial),
):
    print("render full index")
    return base().extend("content", partial)
