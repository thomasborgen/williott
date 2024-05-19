from hypermedia import (
    Anchor,
    Body,
    Button,
    Div,
    Doctype,
    Head,
    Html,
    Image,
    Link,
    Meta,
    Script,
    Svg,
    Title,
)
from hypermedia.models import Element, ElementList, BaseElement


class Path(BaseElement):
    tag: str = "path"


def svg_back() -> Element:
    """Returns a backarrow svg."""

    svg_data = {
        "xmlns": "http://www.w3.org/2000/svg",
        "class": "icon",
        "aria-hidden": "true",
        "focusable": "false",
        "viewBox": "0 0 512 512",
    }

    return Svg(
        Path(
            fill="currentColor",
            d="M9.4 233.4c-12.5 12.5-12.5 32.8 0 45.3l192 192c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L77.3 256 246.6 86.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0l-192 192z",
        ),
        **svg_data,
    )


def svg_home() -> Element:
    svg_data = {
        "xmlns": "http://www.w3.org/2000/svg",
        "class": "icon",
        "aria-hidden": "true",
        "focusable": "false",
        # "viewBox": "0 0 512 512",
        "viewBox": "0 -960 960 960",
    }
    #

    # <path d="M120-240v-80h720v80H120Zm0-200v-80h720v80H120Zm0-200v-80h720v80H120Z"/></svg>

    return Svg(
        Path(
            fill="currentColor",
            d="M120-240v-80h720v80H120Zm0-200v-80h720v80H120Zm0-200v-80h720v80H120Z",
        ),
        **svg_data,
    )
