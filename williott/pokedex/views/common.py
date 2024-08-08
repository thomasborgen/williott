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
        href=f"/pokedex/species/{id}/pokemon/{id}",
        classes=["fab static_size"],
        preload=True,
    )


def render_pokemon_fab_htmx(id: int, target: str):
    return Anchor(
        Div(
            Image(
                alt=f"pokemon with id: {id}",
                src=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png",
            ),
            classes=["fab_circle"],
        ),
        hx_get=f"/pokedex/species/{id}/pokemon/{id}",
        hx_target=target,
        classes=["fab static_size"],
        preload=True,
    )


def render_species_fab_htmx(id: int, target: str):
    return Anchor(
        Div(
            Image(
                alt=f"pokemon with id: {id}",
                src=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png",
            ),
            classes=["fab_circle"],
        ),
        hx_get=f"/pokedex/species/{id}/pokemon/{id}",
        hx_target=target,
        classes=["fab static_size"],
        preload=True,
    )
