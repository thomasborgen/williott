from fastapi import Depends
from hypermedia import Anchor, Button, Div, Header1, Paragraph
from hypermedia.models import Element

from williott.html_utils import icon
from williott.views.base import base


def render_index_partial():
    return Div(
        Header1("Williott", classes=["text_center"]),
        Div(
            Anchor(
                Button(icon(name="search", size="48px"), classes=["fab"]),
                href="/pokedex",
            ),
            Anchor(
                Button(icon(name="question_mark", size="48px"), classes=["fab"]),
                href="/which-one",
            ),
            classes=["stack horizontal"],
        ),
        Paragraph("A collection pokemon related tools/games for my kids"),
        classes=["stack vertical center_items space_evenly full_height"],
    )


def render_index(
    partial: Element = Depends(render_index_partial),
):
    return base().extend("content", partial)
