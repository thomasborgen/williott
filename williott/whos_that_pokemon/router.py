from fastapi import APIRouter

from pathlib import Path

from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi_htmx import htmx, TemplateSpec as Tpl

router = APIRouter(
    prefix="/whos-that-pokemon",
    tags=["whos that pokemon"],
    dependencies=[],
)

TEMPLATE_NAME = "whos_that_pokemon"
TEMPLATE = Jinja2Templates(directory=Path("williott/whos_that_pokemon/templates"))


@router.get("/", response_class=HTMLResponse)
@htmx(Tpl(TEMPLATE_NAME, "index"), Tpl(TEMPLATE_NAME, "index"))
async def root_page(request: Request):
    return {"greeting": "Hello World"}
