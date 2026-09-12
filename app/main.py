"""FinAssist main application module.

Initializes the FastAPI application, sets up Jinja2 template rendering,
and defines core baseline routes.
"""

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

# Application instance with OpenAPI metadata
app = FastAPI(title="FinAssist")

# Configure Jinja2 templates directory
templates = Jinja2Templates(directory="app/templates")


@app.get("/health")
def monitoring() -> dict[str, str]:
    """Health check endpoint.

    Used by hosting platforms (e.g., Render) and orchestrators
    to verify that the server is alive and responding.
    """
    return {"status": "ok"}


@app.get("/")
def home(request: Request):
    """Home page route rendering the initial landing view.

    Passes the HTTP request and template context to Jinja2 to render
    the HTML page with dynamic content.
    """
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"message": "FinAssist is running!"},
    )
