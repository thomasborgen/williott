from hypermedia import (
    Anchor,
    Body,
    Button,
    Div,
    Doctype,
    Head,
    Html,
    Link,
    Meta,
    Script,
    Title,
)
from hypermedia.models import Element, ElementList

from williott.html_utils import icon


def base() -> Element:
    """Create the base page."""
    return ElementList(
        Doctype(),
        Html(
            Head(
                Title(text="Williott - Pokedex"),
                Meta(charset="UTF-8"),
                Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
                Link(rel="stylesheet", href="/static/williott.css"),
                Link(rel="stylesheet", href="/pokedex/static/pokedex.css"),
                Link(
                    rel="stylesheet",
                    href="https://fonts.googleapis.com/icon?family=Material+Icons",
                ),
                slot="head",
            ),
            Body(
                header(),
                Div(id="content", slot="content", classes=["content"]),
            ),
            Script(
                src="https://unpkg.com/htmx.org@1.9.10",
                integrity="sha384-D1Kt99CQMDuVetoL1lrYwg5t+9QdHe7NLX/SoJYkXDFfX37iInKRy5xLSi8nO7UC",
                crossorigin="anonymous",
            ),
            Script(src="/static/auto_playback.js"),
            lan="en",
        ),
    )


def header() -> Element:
    """Create the header page with navigation."""

    return Div(
        Button(
            icon(name="arrow_back_ios", size="48px"),
            onclick="history.back()",
            classes=["fab"],
        ),
        Anchor(Button(icon(name="menu", size="48px"), classes=["fab"]), href="/"),
        classes=["stack space_between padding_small"],
    )
