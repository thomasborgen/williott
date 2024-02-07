from random import randint
from fastapi import APIRouter

from pathlib import Path

from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi_htmx import htmx, TemplateSpec as Tpl
import requests

from williott.constants import POKEAPI_URL

router = APIRouter(
    prefix="/which-one",
    tags=["Which one"],
    dependencies=[],
)

TEMPLATE_NAME = "which_one"
TEMPLATE = Jinja2Templates(directory=Path("williott/which_one/templates"))


def construct_game():
    pokemon = [randint(1, 151), randint(1, 151), randint(1, 151), randint(1, 151)]
    target = pokemon[randint(0, 3)]

    result = requests.get(f"{POKEAPI_URL}{target}").json()

    return {"pokemon": pokemon, "target": target, "target_name": result["name"]}


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
