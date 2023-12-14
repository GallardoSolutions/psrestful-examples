from datetime import datetime

import requests
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.config import Config

from filters import humanize_ts
from utils import gen_all_products

config_env = Config('.env')

PS_RESTFUL_KEY = config_env.get("PS_RESTFUL_KEY", default="p")
PS_RESTFUL_HOST = 'https://api.psrestful.com'

app = FastAPI(debug=True)

templates = Jinja2Templates(directory="templates")

templates.env.filters["humanize_ts"] = humanize_ts

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("inventory-levels.html", {"request": request})


@app.get("/products")
async def get_products(request: Request, supplier_code: str, environment: str):
    url = f"{PS_RESTFUL_HOST}/v2.0.0/suppliers/{supplier_code}/sellable-products/"
    data = {
        'environment': environment
    }
    headers = {
        'x-api-key': PS_RESTFUL_KEY,
        "accept": "application/json"
    }
    response = requests.get(url, params=data, headers=headers)
    context = {'response_code': response.status_code, 'environment': environment, 'supplier_code': supplier_code}
    if response.status_code == 200:
        all_variants = response.json()['ProductSellableArray']['ProductSellable']
        all_products = gen_all_products(all_variants)
        context |= {
            'products': all_products,
            'no_products': len(all_products),
            'error': None,
        }
    else:
        context |= {
            'products': [],
            'error': response.text,
        }
    context["request"] = request
    return templates.TemplateResponse("products.html", context)


@app.get("/inventory/{supplier_code}/{product_id}")
async def inventory(request: Request, supplier_code: str, product_id: str, environment: str):
    url = f"{PS_RESTFUL_HOST}/v2.0.0/suppliers/{supplier_code}/inventory/{product_id}"
    data = {
        'environment': environment
    }
    headers = {
        'x-api-key': PS_RESTFUL_KEY,
        "accept": "application/json"
    }
    response = requests.get(url, params=data, headers=headers)
    context = {'response_code': response.status_code, 'request': request, 'environment': environment,
               'supplier_code': supplier_code, 'product_id': product_id, 'error': None}
    if response.status_code == 200:
        data = response.json()
        context['PartInventory'] = data['Inventory']['PartInventoryArray']['PartInventory']
        for inv in context['PartInventory']:
            inv['lastModified'] = datetime.fromisoformat(inv['lastModified'])

    else:
        context['error'] = response.text
    return templates.TemplateResponse("inventory.html", context)
