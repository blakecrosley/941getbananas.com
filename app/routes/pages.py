from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse, Response, RedirectResponse
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

# AI Context Files (per llmstxt.org specification)
# Static: https://941getbananas.com/llms.txt

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


@router.get("/llms.txt", response_class=PlainTextResponse)
async def llms_txt():
    """AI context file per llmstxt.org specification."""
    content = """# 941 Get Bananas

> Banana tracking made simple - never run out of bananas again.

## About

941 Get Bananas is a playful banana tracking app from 941 Apps, LLC. Part of the 941 ecosystem of simple, necessary applications built with care.

## Features

- Track your banana inventory
- Get reminders when running low
- Simple, delightful interface
- Part of the 941 Apps family

## Company

941 Get Bananas is developed by 941 Apps, LLC, a design and engineering studio based in Pasadena, CA.

- Website: https://941apps.com
- Contact: hello@941apps.com

## Related

- 941 Apps: https://941apps.com
- Ace Citizenship: https://acecitizenship.app
- 941 Return: https://941return.com

## Technical

- Platform: Web (FastAPI + HTMX)
- Deployment: Railway
"""
    return PlainTextResponse(content=content.strip())


@router.get("/.well-known/llms.txt")
async def well_known_llms_txt():
    """Redirect .well-known/llms.txt to main llms.txt per spec."""
    return RedirectResponse(url="/llms.txt", status_code=301)


@router.get("/humans.txt", response_class=PlainTextResponse)
async def humans_txt():
    """Site credits and information for humans."""
    content = """/* TEAM */
Developer: Blake Crosley
Site: https://blakecrosley.com
Location: Pasadena, CA

/* COMPANY */
Name: 941 Apps, LLC
Site: https://941apps.com
Contact: hello@941apps.com

/* SITE */
Last update: 2025-01-12
Language: English
Standards: HTML5, CSS3
Platform: FastAPI, HTMX, Alpine.js, Bootstrap 5
Hosting: Railway
"""
    return PlainTextResponse(content=content.strip())


@router.get("/.well-known/security.txt", response_class=PlainTextResponse)
async def security_txt():
    """Security contact information per security.txt standard."""
    content = """# Security Policy for 941 Get Bananas
# https://941getbananas.com

Contact: mailto:security@941apps.com
Expires: 2026-12-31T23:59:59.000Z
Preferred-Languages: en
Canonical: https://941getbananas.com/.well-known/security.txt

# Policy
# We take security seriously. If you discover a vulnerability,
# please report it responsibly to security@941apps.com.
# We aim to respond within 48 hours.
"""
    return PlainTextResponse(content=content.strip())
