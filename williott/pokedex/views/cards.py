import requests
from fastapi import Depends
from hypermedia import Button, Div, Image
from hypermedia.models import ElementList

from williott.pokemon.dependencies import get_pokemon
from williott.pokemon.models import Pokemon

CARD_API: str = "https://api.pokemontcg.io/v2/cards?q=nationalPokedexNumbers:{id}{query}&select=id,images"
# (-name:*alola* OR -name:*test*)


def render_cards_partial(pokemon: Pokemon = Depends(get_pokemon)):
    query = ""
    if pokemon.is_default:
        # get exact match on name.
        query = f" !name:{pokemon.identifier}"

    else:
        name = pokemon.species.identifier

        form_name = pokemon.identifier.replace(name, "").replace("-", "")

        query = f" name:*{form_name}*"

    result = requests.get(CARD_API.format(id=str(pokemon.species_id), query=query))

    the_json = result.json()

    data = the_json["data"]

    images = [{"id": entry["id"], "url": entry["images"]["small"]} for entry in data]

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
