from random import randint
from fastapi import APIRouter, Depends

from fastapi import Request
from fastapi.responses import HTMLResponse
from hypermedia import full, htmx
from hypermedia.models import Element

from williott.which_one.views.game import render_game, render_game_partial
from williott.which_one.views.index import render_index, render_index_partial

router = APIRouter(
    prefix="/which-one",
    tags=["Which one"],
    dependencies=[],
)


def construct_game():
    pokemon = [randint(1, 151), randint(1, 151), randint(1, 151), randint(1, 151)]
    target = database[str(pokemon[randint(0, 3)])]

    return {"pokemon": pokemon, "target": target}


def construct_index():
    return {
        "name": "Pikachu",
        **construct_game(),
    }


@router.get("/", response_class=HTMLResponse)
@htmx
async def index(
    request: Request,
    partial: Element = Depends(render_index_partial),
    full: Element = Depends(full(render_index)),
) -> None:
    """Return the index page."""
    pass


@router.get("/{generation_id}", response_class=HTMLResponse)
@htmx
async def generation(
    request: Request,
    partial: Element = Depends(render_game_partial),
    full: Element = Depends(full(render_game)),
) -> None:
    """Return the game page."""
    pass
