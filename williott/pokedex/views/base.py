from hypermedia import Anchor, Button, Div, Link
from hypermedia.models import Element, ElementList

from williott.html_utils import icon

from williott.views.base import real_base


def base() -> Element:
    """Create the base page."""
    base = real_base()
    base.extend(
        "head",
        Link(rel="stylesheet", href="/pokedex/static/pokedex.css"),
    )
    base.extend(
        "body",
        ElementList(
            header(),
            Div(id="content", slot="content", classes=["content"]),
        ),
    )
    return base


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
