from hypermedia import Anchor, Div, Image


def render_pokemon_fab(id: int):
    return Anchor(
        Div(
            Image(
                alt=f"pokemon with id: {id}",
                src=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png",
            ),
            classes=["fab_circle"],
        ),
        href=f"/pokedex/pokemon/{id}",
        classes=["fab static_size"],
    )
