# A FastAPI project to get sorted parts based on total sales

## What is this code about?

This code is a FastAPI project that uses `PSRESTful API` to get sorted parts based on total sales.

## Extra APIs

We have introduced `Extra` APIs not implemented in PromoStandards but in PSRESTful API.

These Extra APIs are available in the `extra` namespace and only for enterprise clients

- `GET /extra/v1/suppliers/` - Get all supported suppliers
- `GET /extra/v1/products/` - Get all product with several filters including by supplier
- `GET /extra/v1/products/{extra_id}/` - Get the product details
- `GET /extra/v1/products/:extra_id/sorted-parts?days=60/` - Get the sorted parts for a product based on total sales in the last 60 days

It is a simple example, but it shows how to use `PSRESTful API` to sorted parts for a product.

We used [Bootstrap](https://getbootstrap.com/) and [HTMX](https://htmx.org/) to make the UI more user-friendly.

But the main focus is on how to use `PSRESTful API` to get sorted parts for a product. Not the UI.

We believe it will help you understand how easy is to integrate your backend to use `PSRESTful API`.

Even though our example is in Python, the example is easy enough to be ported to any other programming language.

## Installation

```bash
pyenv virtualenv sorted_parts
pyenv activate sorted_parts
pip install -r requirements.txt
```

## Before running the project

- Register in [PSRESTful](https://psrestful.com) and get the `API key`
- Create a .env file in the root directory of the project and add `PS_RESTFUL_KEY` variable with the API key value
- Enter your supplier passwords at least for one Supplier 
- Run `uvicorn main:app --port 8000 --host 127.0.0.1 --workers 1`
- Open http://localhost:8000/ in your browser

## Tools used

- [FastAPI](https://fastapi.tiangolo.com/)
- [PyEnv](https://github.com/pyenv/pyenv)
- [PSRESTful](https://psrestful.com)
- [Bootstrap](https://getbootstrap.com/)
- [HTMX](https://htmx.org/)
- [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/)

## List of supported suppliers

[Integrated Suppliers](https://psrestful.com/integrated-suppliers/)
