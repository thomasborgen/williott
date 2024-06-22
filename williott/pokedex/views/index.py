from fastapi import Depends
from hypermedia import Button, Div, Header2
from hypermedia.models import Element

from williott.pokedex.views.base import base


def render_index_partial():
    generations = [
        Button(
            text=str(gen),
            hx_get=f"/pokedex/generations/{gen}",
            hx_target="#content",
            hx_swap="innerHTML",
            hx_push_url="true",
            preload=True,
        )
        for gen in range(1, 10)
    ]
    return Div(
        Div(
            Header2(classes=["text_center"], text="PokeDex"),
            classes=["stack vertical center_items"],
        ),
        Div(
            *generations,
            classes=[
                "stack auto_size_flex_items wrap spacing_medium horizontal center_items"
            ],
        ),
        classes=["stack vertical spacing_medium"],
    )


def render_index(
    partial: Element = Depends(render_index_partial),
):
    return base().extend("content", partial)
