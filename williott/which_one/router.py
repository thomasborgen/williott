from random import randint
from fastapi import APIRouter

from pathlib import Path

from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi_htmx import htmx, TemplateSpec as Tpl

from williott.pokemon.constants import database

router = APIRouter(
    prefix="/which-one",
    tags=["Which one"],
    dependencies=[],
)

TEMPLATE_NAME = "which_one"
TEMPLATE = Jinja2Templates(directory=Path("williott/which_one/templates"))


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
@htmx(
    Tpl(TEMPLATE_NAME, "game"),
    Tpl(TEMPLATE_NAME, "index"),
    construct_game,
    construct_index,
)
async def root_page(request: Request):
    pass
