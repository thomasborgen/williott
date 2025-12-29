import json

from hypermedia import (
    Body,
    Div,
    Doctype,
    Element,
    ElementList,
    Head,
    Html,
    Link,
    Main,
    Meta,
    Script,
    Title,
)


def base() -> Element:
    """Create the base page."""
    htmx_config = {
        "defaultSwapStyle": "innerHTML",
        "globalViewTransitions": True,
        "history": False,
        "refreshOnHistoryMiss": True,
        "allowNestedOobSwaps": True,
        "historyCacheSize": 0,
    }

    return ElementList(
        Doctype(),
        Html(
            Head(
                Meta(charset="UTF-8"),
                Meta(
                    name="viewport",
                    content="width=device-width, height=device-height, initial-scale=1.0",
                ),
                Meta(name="htmx-config", content=json.dumps(htmx_config)),
                # Link(
                #     href="https://cdn.jsdelivr.net/npm/daisyui@4.12.14/dist/full.min.css",
                #     rel="stylesheet",
                #     type="text/css",
                # ),
                Link(
                    rel="stylesheet",
                    href="/static/css/williott.css",
                ),
                Link(
                    rel="stylesheet",
                    href="https://fonts.googleapis.com/icon?family=Material+Icons",
                ),
                Link(
                    rel="stylesheet",
                    href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0",
                ),
                # Script(src="https://cdn.tailwindcss.com"),
                Script(src="/static/javascript/htmx.min.js"),
                Script(src="/static/javascript/audio_event_attacher.js"),
                Script(src="https://unpkg.com/hyperscript.org@0.9.12"),
                Title("Hirawilliott - home"),
                slot="head",
            ),
            body(),
            lang="no-nb",
            data_theme="cupcake",  # type: ignore
            class_="h-screen",
        ),
    )


def body() -> Body:
    """Create page base."""
    return Body(
        Div(id="indicator"),
        Main(
            id="main",
            slot="main",
            class_="h-dvh w-full overflow-hidden",
        ),
        Div(id="toast_container", class_="toast toast-start toast-middle"),
        hx_indicator="#indicator",
        hx_history="false",
        class_="h-screen w-screen",
    )
