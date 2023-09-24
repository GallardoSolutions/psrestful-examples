# A FastAPI project to check order status

## What is this code about?

This code is a FastAPI project that uses `PSRESTful API` to check order status.

We show step by step how to use `PSRESTful API` to check order status for a supplier implementing `PromoStandards`.

It is a simple example, but it shows how to use `PSRESTful API` to check order status for a supplier.

We used [Bootstrap](https://getbootstrap.com/) and [JQuery](https://jquery.com/) to make the UI more user-friendly.

But the main focus is on how to use `PSRESTful API` to check order status for a supplier. Not the UI.

We believe it will help you understand how easy is to integrate your backend to use `PSRESTful API` to check order 
status for all suppliers we support.

In our case we use the option to check order status based on query_type=3(Last Update Search) that allows to query 
based on all orders with an update time greater than the value specified in `statusTimeStamp`. In our 
[Standards documentation](https://docs.psrestful.com/standards/) you can find more information about this option.

Even though our example is in Python, the example is easy enough to be ported to any other programming language.

## Installation

```bash
pyenv virtualenv order_status
pyenv activate order_status
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
- [JQuery](https://jquery.com/)
- [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/)

## List of supported suppliers

[Integrated Suppliers](https://psrestful.com/integrated-suppliers/)
