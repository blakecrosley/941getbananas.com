from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.routes import pages

app = FastAPI(
    title="Get Bananas",
    description="The hand-drawn shopping list for your whole family",
)

# Static files
app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent / "static"),
    name="static",
)

# Templates
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")

# Include routes
app.include_router(pages.router)
