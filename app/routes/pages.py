from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse, Response
from fastapi.templating import Jinja2Templates
from pathlib import Path

router = APIRouter()
templates = Jinja2Templates(directory=Path(__file__).parent.parent / "templates")

SITE_URL = "https://941getbananas.com"


@router.get("/robots.txt", response_class=PlainTextResponse)
async def robots_txt():
    """Serve robots.txt - welcoming to SEO and AI crawlers."""
    content = """# 941getbananas.com robots.txt
# Welcome to all search engines and AI crawlers

User-agent: *
Allow: /

# SEO Crawlers
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: Slurp
Allow: /

User-agent: DuckDuckBot
Allow: /

User-agent: Applebot
Allow: /

User-agent: Yandex
Allow: /

User-agent: Baiduspider
Allow: /

# AI Crawlers - Welcome
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: Anthropic-ai
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Bytespider
Allow: /

User-agent: CCBot
Allow: /

User-agent: cohere-ai
Allow: /

User-agent: meta-externalagent
Allow: /

User-agent: Amazonbot
Allow: /

Sitemap: https://941getbananas.com/sitemap.xml
"""
    return PlainTextResponse(content=content)


@router.get("/sitemap.xml")
async def sitemap():
    """Generate sitemap for search engines."""
    from datetime import datetime

    lastmod = datetime.now().strftime("%Y-%m-%d")

    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>{SITE_URL}/</loc>
        <lastmod>{lastmod}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>{SITE_URL}/privacy</loc>
        <lastmod>{lastmod}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.3</priority>
    </url>
    <url>
        <loc>{SITE_URL}/terms</loc>
        <lastmod>{lastmod}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.3</priority>
    </url>
    <url>
        <loc>{SITE_URL}/support</loc>
        <lastmod>{lastmod}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.5</priority>
    </url>
</urlset>"""

    return Response(content=sitemap_xml, media_type="application/xml")


@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/privacy")
async def privacy(request: Request):
    return templates.TemplateResponse("privacy.html", {"request": request})


@router.get("/support")
async def support(request: Request):
    return templates.TemplateResponse("support.html", {"request": request})


@router.get("/terms")
async def terms(request: Request):
    return templates.TemplateResponse("terms.html", {"request": request})
