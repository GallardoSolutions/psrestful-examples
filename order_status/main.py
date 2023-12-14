from datetime import datetime

import requests
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.config import Config

config_env = Config('.env')

PS_RESTFUL_KEY = config_env.get("PS_RESTFUL_KEY", default="p")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("order-status.html", {"request": request})


@app.get("/orders/")
async def orders(supplier_code: str, environment: str, status_timestamp: datetime):
    url = f"https://api.psrestful.com/v1.0.0/suppliers/{supplier_code}/order-status-details/"
    data = {
        'query_type': 3,
        'status_timestamp': str(status_timestamp),
        'environment': environment
    }
    headers = {
        'x-api-key': PS_RESTFUL_KEY,
        "accept": "application/json"
    }
    response = requests.get(url, params=data, headers=headers)
    return response.json()
