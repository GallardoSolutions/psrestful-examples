import requests
from fastapi import FastAPI, Request, Query
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi_htmx import htmx_init

from starlette.config import Config

config_env = Config('.env')

PS_RESTFUL_KEY = config_env.get("PS_RESTFUL_KEY", default="p")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")
htmx_init(templates=templates)


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/sorted-parts")
async def sorted_parts(request: Request, product_id: int = Query(...)):
    url = f"https://api.psrestful.com/extra/v1/products/{product_id}/sorted-parts?days=60"
    headers = {
        'x-api-key': PS_RESTFUL_KEY,
        "accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    resp = response.json()

    return templates.TemplateResponse("sorted_parts.html", {"response": resp,
                                                            "request": request})
