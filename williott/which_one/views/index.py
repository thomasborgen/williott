from fastapi import Depends
from hypermedia import Anchor, Div, Header2
from hypermedia.models import Element

from williott.which_one.views.base import base, header


def render_index_partial():
    generations = [
        Anchor(
            str(gen),
            classes=["fab"],
            href=f"/which-one/{gen}",
            preload=True,
        )
        for gen in range(1, 10)
    ]
    return Div(
        Div(
            Header2("Choose Generation", classes=["text_center"]),
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
    return base().extend("header", header(back_path="/")).extend("content", partial)
