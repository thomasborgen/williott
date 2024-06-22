import requests
from fastapi import Depends
from hypermedia import Button, Div, Image
from hypermedia.models import ElementList

from williott.pokemon.dependencies import get_species
from williott.pokemon.models import Species

CARD_API: str = "https://api.pokemontcg.io/v2/cards?q=nationalPokedexNumbers:"


def render_cards_partial(
    species: Species = Depends(get_species),
):
    result = requests.get(CARD_API + str(species.id))

    images = [
        {"id": entry["id"], "url": entry["images"]["small"]}
        for entry in result.json()["data"]
    ]

    image_elements = [
        ElementList(
            Button(
                Image(src=image["url"]),
                popovertarget=f"image_{image['id']}",
                classes=["list image_button"],
            ),
            Div(
                Button(
                    Image(src=image["url"]),
                    popovertarget=f"image_{image['id']}",
                    classes=["image_button"],
                ),
                popover=True,
                id=f"image_{image['id']}",
                classes=["popover"],
            ),
        )
        for image in images
    ]

    return Div(
        *image_elements,
        classes=["cards stack horizontal wrap spacing_medium space_evenly"],
    )
