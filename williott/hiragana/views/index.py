from typing import Annotated
from fastapi import Depends
from hypermedia import (
    Div,
    Element,
    Form,
    Input,
    Label,
    Span,
    Title,
)

from williott.components import base


def _row_renderer(characters: list[str]) -> Element:
    return Label(
        Input(
            type="checkbox",
            name="characters",
            value=",".join(characters),
            class_="checkbox checkbox-primary",
        ),
        Span(
            ", ".join(characters),
        ),
        class_="label",
    )


def render_index_partial() -> Element:
    """Render only index form."""
    return Div(
        Form(
            _row_renderer(["あ", "い", "う", "え", "お"]),
            _row_renderer(["か", "き", "く", "け", "こ"]),
            _row_renderer(["さ", "し", "す", "せ", "そ"]),
            _row_renderer(["た", "ち", "つ", "て", "と"]),
            _row_renderer(["な", "に", "ぬ", "ね", "の"]),
            _row_renderer(["は", "ひ", "ふ", "へ", "ほ"]),
            _row_renderer(["ま", "み", "む", "め", "も"]),
            _row_renderer(["や", "ゆ", "よ"]),
            _row_renderer(["ら", "り", "る", "れ", "ろ"]),
            _row_renderer(["わ", "を", "ん"]),
            Input(
                type="submit",
                value="Start",
                class_="btn btn-primary w-100 absolute bottom-4 right-4 left-4",
            ),
            hx_get="/hiragana/game",
            hx_push_url="true",
            hx_target="#main",
            class_="flex flex-col gap-4 p-4 items-start justify-center",
        ),
        class_="min-h-full w-full",
    )


def render_index(
    partial: Annotated[Element, Depends(render_index_partial)],
) -> Element:
    """Render the full page, with index form."""
    return (
        base()
        .extend("head", Title("Hirawilliott - Hiragana Practice"))
        .extend("main", partial)
    )
