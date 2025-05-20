from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
STATIC_DIR = "static"


# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up the Jinja2 templates directory
templates = Jinja2Templates(directory="templates")

# Home route
@app.get("/", response_class=HTMLResponse)
def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# About route
@app.get("/about", response_class=HTMLResponse)
def read_about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})
