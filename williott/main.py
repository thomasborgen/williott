from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


from fastapi import APIRouter

from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi_htmx import htmx, htmx_init, TemplateSpec as Tpl

from williott.whos_that_pokemon.router import (
    router as whos_that_pokemon_router,
    TEMPLATE as whos_that_pokemon_template,
    TEMPLATE_NAME as whos_that_pokemon_template_name,
)

from williott.which_one.router import (
    router as which_one_router,
    TEMPLATE as which_one_template,
    TEMPLATE_NAME as which_one_template_name,
)

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(whos_that_pokemon_router)
app.include_router(which_one_router)

app.mount("/static", StaticFiles(directory="williott/static/"), name="static")
app.mount(
    "/which-one/static",
    StaticFiles(directory="williott/which_one/static/"),
    name="which-one-static",
)


templates = {
    "main": Jinja2Templates(directory=Path("williott/templates")),
    whos_that_pokemon_template_name: whos_that_pokemon_template,
    which_one_template_name: which_one_template,
}

htmx_init(templates=templates)


@app.get("/", response_class=HTMLResponse)
@htmx(Tpl("main", "index"), Tpl("main", "index"))
async def root_page(request: Request):
    print("what")
    return {"greeting": "Hello World"}
