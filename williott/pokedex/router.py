from typing import Any

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
# from fastapi_htmx import htmx

from hypermedia import full, htmx
from hypermedia.models import Element

from williott.pokedex.views.index import render_index, render_index_partial

router = APIRouter(
    prefix="/pokedex",
    tags=["Pokedex"],
    dependencies=[],
)


@router.get("/{generation_id}", response_class=HTMLResponse)
@htmx
async def index(
    request: Request,
    partial: Element = Depends(render_index_partial),
    full: Element = Depends(full(render_index)),
) -> None:
    """Return the index page."""
    pass


# @router.get("/", response_class=HTMLResponse)
# @htmx(
#     construct_generation_list,
#     construct_index,
# )
# async def index(request: Request, generation: int | None = None):
#     return construct_index(generation)


# @router.post("/{generation}", response_class=HTMLResponse)
# @htmx(
#     construct_generation_list,
#     construct_index,
# )
# async def root_page(request: Request, generation: int | None = None):
#     pass


# @router.get("/pokemon/{id}", response_class=HTMLResponse)
# @htmx(
#     construct_pokemon,
# )
# async def pokemon(request: Request, id: int):
#     return construct_pokemon(id)
