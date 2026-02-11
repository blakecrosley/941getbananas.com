from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from starlette.middleware.base import BaseHTTPMiddleware

from app.routes import pages
from app.security.headers import SecurityHeadersMiddleware
from app.security.logging import SecurityLogMiddleware
from app.security.rate_limit import RateLimitMiddleware
from app.cache_assets import build_asset_map, make_asset_url


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
    docs_url=None,  # Disable Swagger UI in production
    redoc_url=None,  # Disable ReDoc in production
    openapi_url=None,  # Disable OpenAPI schema entirely
)

# Middleware (order matters: last added = first executed)
app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(HeadRequestMiddleware)
app.add_middleware(RateLimitMiddleware)
app.add_middleware(SecurityLogMiddleware, site_name="941getbananas.com")

# Static files
app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent / "static"),
    name="static",
)

# Templates
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")

# Content-hash asset versioning
_static_dir = Path(__file__).parent / "static"
_asset_map = build_asset_map(_static_dir)
templates.env.globals["asset"] = lambda path: make_asset_url(_asset_map, path)

# Early Hints: preload Link header for critical CSS
app.state.preload_links = [
    f'<{make_asset_url(_asset_map, "css/custom.css")}>; rel=preload; as=style',
]

# Include routes
app.include_router(pages.router)
