from hypermedia import (
    Body,
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
                slot="head",
            ),
            Body(
                Div(id="content", slot="content", classes=["content"]),
            ),
            Script(
                src="https://unpkg.com/htmx.org@1.9.10",
                integrity="sha384-D1Kt99CQMDuVetoL1lrYwg5t+9QdHe7NLX/SoJYkXDFfX37iInKRy5xLSi8nO7UC",
                crossorigin="anonymous",
            ),
            Script(src="/static/hx-json-form.js"),
            lan="en",
        ),
    )
