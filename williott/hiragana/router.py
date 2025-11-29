from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from hypermedia import Element
from hypermedia.fastapi import full, htmx


from williott.hiragana.views.game import render_game, render_game_partial
from williott.hiragana.views.index import (
    render_index,
    render_index_partial,
)


router = APIRouter(
    prefix="/hiragana",
    dependencies=[],
)


@router.get("", response_class=HTMLResponse)
@htmx
async def hiragana_index(
    request: Request,
    partial: Element = Depends(render_index_partial),
    full: Element = Depends(full(render_index)),
) -> None:
    """Return the index page."""


@router.get("/game", response_class=HTMLResponse)
@htmx
async def game_index(
    request: Request,
    partial: Element = Depends(render_game_partial),
    full: Element = Depends(full(render_game)),
) -> None:
    """Return the index page."""
