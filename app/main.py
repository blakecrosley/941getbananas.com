from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from starlette.middleware.base import BaseHTTPMiddleware

from app.routes import pages


class HeadRequestMiddleware(BaseHTTPMiddleware):
    """Handle HEAD requests by converting them to GET and stripping the body.

    FastAPI doesn't automatically support HEAD method for all routes.
    This middleware ensures HEAD requests work for SEO tools like Googlebot.
    """

    async def dispatch(self, request, call_next):
        if request.method == "HEAD":
            request.scope["method"] = "GET"
            response = await call_next(request)
            response.body = b""
            return response
        return await call_next(request)


app = FastAPI(
    title="Get Bananas",
    description="The hand-drawn shopping list for your whole family",
)

# Middleware
app.add_middleware(HeadRequestMiddleware)

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
