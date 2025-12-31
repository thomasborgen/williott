from fastapi import Depends
from hypermedia import Anchor, Button, Div, Header1, HorizontalRule, Paragraph
from hypermedia.models import Element

from williott.html_utils import icon
from williott.components import base


def render_index_partial():
    return Div(
        Div(
            Div(
                Header1("Williott", class_="text-5xl font-bold"),
                Paragraph("A collection pokemon related tools/games for my kids"),
                Div(class_="divider"),
                Div(
                    Button(
                        icon(name="translate"),
                        class_="btn btn-circle",
                        hx_get="/hiragana",
                        hx_push_url="true",
                        hx_target="main",
                    ),
                    Button(icon(name="search"), class_="btn btn-circle"),
                    Button(icon(name="question_mark"), class_="btn btn-circle"),
                    class_="flex flex-col items-center gap-2",
                ),
                class_="max-w-md",
            ),
            class_="hero-content text-center flex flex-col gap-4",
        ),
        class_="hero bg-base-200 min-h-screen",
    )

    return Div(
        Header1("Williott hei", classes=["text_center"]),
        Div(
            Anchor(
                Button(icon(name="translate", size="48px"), classes=["fab"]),
                href="/hiragana",
            ),
        ),
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
        classes=["flex flex-col items-center justify-center"],
    )


def render_index(
    partial: Element = Depends(render_index_partial),
):
    return base().extend("main", partial)
