import urllib
from random import randint

from fastapi import Depends
from hypermedia import Audio, Div, Header2, Image
from hypermedia.models import Element

from williott.pokemon.constants import OFFICIAL_ART_PATH
from williott.pokemon.dependencies import get_generation
from williott.pokemon.models import GenerationRead
from williott.which_one.views.base import base, header


def render_game_partial(
    generation: GenerationRead = Depends(get_generation),
):
    species = generation.species
    options = [species[randint(0, len(species) - 1)] for _ in range(4)]
    target = options[randint(0, 3)]

    option_elements = [
        Div(
            Image(
                src=OFFICIAL_ART_PATH.format(id=option.id),
                classes=["target"],
            ),
            preload=True,
            hx_get=f"/which-one/{generation.id}",
            hx_swap="innerHTML swap:1s",
            hx_target="#content",
            classes=["target"],
            **{"preload-images": "true"},
        )
        if option.id == target.id
        else Div(
            Image(
                src=OFFICIAL_ART_PATH.format(id=option.id),
                classes=["wrong"],
            ),
            classes=["wrong"],
        )
        for option in options
    ]

    return Div(
        Div(
            Header2(target.identifier, classes=["text_center"]),
            classes=["stack vertical center_items"],
        ),
        Div(
            Div(
                *option_elements[:2],
                classes=["stack horizontal spacing_medium"],
            ),
            Div(
                *option_elements[2:],
                classes=["stack horizontal spacing_medium"],
            ),
            classes=["stack vertical spacing_medium"],
        ),
        Audio(
            src=urllib.parse.quote(
                f"/speak/english/Which of these pokemon is, {target.identifier}"
            ),
            style={"display": "none"},
            autoplay="true",
        ),
        id="game",
        classes=["stack vertical spacing_medium"],
    )


def render_game(
    partial: Element = Depends(render_game_partial),
):
    return (
        base()
        .extend("header", header(back_path="/which-one"))
        .extend("content", partial)
    )
