import random
from typing import Annotated
from fastapi import Depends
from hypermedia import H2, Audio, Div, Element, Figure, Image, Title

from williott.components import base
from williott.hiragana.dependencies import get_characters

from williott.hiragana.database import db, Hiragana


def _choice_renderer(hiragana: Hiragana, correct: bool = False) -> Element:
    audio = None

    if not correct:
        ssml = f'<say-as interpret-as="characters">{hiragana.character}</say-as><break strength="strong"/>{hiragana.word}'
        audio = Audio(
            src=f"/speak?text={ssml}",
            class_="hidden",
            id=f"audio_{hiragana.romaji}",
        )

    return Div(
        Div(
            H2(hiragana.character, class_="card-title text-7xl mx-auto"),
            class_="card-body",
        ),
        Figure(
            Image(
                src=f"/hiragana/static/hiragana/{hiragana.image}",
                alt="Shoes",
                class_="max-w-full max-h-full",
            ),
            class_="opacity-0",
            _="on load wait for 4s then transition opacity to 1",
        ),
        audio and audio or "",
        id=hiragana.romaji,
        class_="card bg-base-100 shadow-xl grid grid-rows-2",
        _=f"on click transition my background-color to {'"green"' if correct else '"red"'} over 200ms",
        hx_get="" if correct else None,
        hx_trigger="click delay:1s" if correct else None,
        hx_target="#main",
    )


def render_game_partial(
    characters: Annotated[list[str], Depends(get_characters)],
) -> Element:
    """Render only game form."""

    num_choices = min(4, len(characters))
    random.shuffle(characters)
    choices = characters[:num_choices]

    target_index = random.randint(0, num_choices - 1)
    target_hiragana = db.get(choices[target_index])[0]

    character = f'<say-as interpret-as="characters">{target_hiragana.character}</say-as><break strength="strong"/><say-as interpret-as="characters">{target_hiragana.character}</say-as>'

    speech = f'{character}<break time="1000ms"/>{target_hiragana.word}'

    return Div(
        *[
            _choice_renderer(db.get(hiragana)[0], correct=i == target_index)
            for i, hiragana in enumerate(choices)
        ],
        Audio(
            src=f"/speak?text={speech}",
            class_="hidden",
            autoplay="true",
        ),
        class_="h-full w-full grid grid-cols-2 grid-rows-2 gap-3 p-3",
    )


def render_game(
    partial: Element = Depends(render_game_partial),
) -> Element:
    """Render the full page, with game form."""
    return (
        base()
        .extend("head", Title("Hirawilliott - Hiragana Practice"))
        .extend("main", partial)
    )
