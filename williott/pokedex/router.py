from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse

from hypermedia import full, htmx
from hypermedia.models import Element

from williott.pokedex.views.cards import render_cards_partial
from williott.pokedex.views.generations import (
    render_generations,
    render_generations_partial,
)
from williott.pokedex.views.index import render_index, render_index_partial
from williott.pokedex.views.pokemon import render_pokemon, render_pokemon_partial

router = APIRouter(
    prefix="/pokedex",
    tags=["Pokedex"],
    dependencies=[],
)


@router.get("/", response_class=HTMLResponse)
@htmx
async def index(
    request: Request,
    partial: Element = Depends(render_index_partial),
    full: Element = Depends(full(render_index)),
) -> None:
    """Return the index page."""
    pass


@router.get("/generations/{generation_id}", response_class=HTMLResponse)
@htmx
async def generation(
    request: Request,
    partial: Element = Depends(render_generations_partial),
    full: Element = Depends(full(render_generations)),
) -> None:
    """Return the index page."""
    pass


@router.get("/pokemon/{pokemon_id}", response_class=HTMLResponse)
@htmx
async def pokemon(
    request: Request,
    partial: Element = Depends(render_pokemon_partial),
    full: Element = Depends(full(render_pokemon)),
) -> None:
    """Return the index page."""
    pass


@router.get("/cards/{pokemon_id}", response_class=HTMLResponse)
@htmx
async def cards(
    request: Request,
    partial: Element = Depends(render_cards_partial),
) -> None:
    """Return the index page."""
    pass
