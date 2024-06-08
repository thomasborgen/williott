from hypermedia import Span
from hypermedia.models import Element


def icon(*, name: str, size: str = "24px") -> Element:
    """Creates a Span element with a material icon."""
    return Span(text=name, classes=["material-icons"], style=f"font-size: {size}")
