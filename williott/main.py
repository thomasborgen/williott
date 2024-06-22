from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from hypermedia import full, htmx
from hypermedia.models import Element


from williott.pokedex.router import (
    router as pokedex_router,
)

from williott.which_one.router import (
    router as which_one_router,
)

from williott.speak.router import (
    router as speak_router,
)
from williott.views.index import render_index, render_index_partial

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pokedex_router)
app.include_router(which_one_router)
app.include_router(speak_router)

app.mount("/static", StaticFiles(directory="williott/static/"), name="static")
app.mount(
    "/which-one/static",
    StaticFiles(directory="williott/which_one/static/"),
    name="which-one-static",
)
app.mount(
    "/pokedex/static",
    StaticFiles(directory="williott/pokedex/static/"),
    name="pokedex",
)


@app.get("/", response_class=HTMLResponse)
@htmx
async def index(
    request: Request,
    partial: Element = Depends(render_index_partial),
    full: Element = Depends(full(render_index)),
) -> None:
    """Return the index page."""
    pass
