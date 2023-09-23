A FastAPI project to check order status

## Installation

```bash
pyenv virtualenv order_status
pyenv activate order_status
pip install -r requirements.txt
```

# Before running the project

- Register in [PSRESTful](https://psrestful.com) and get the `API key`
- Create a .env file in the root directory of the project and add PS_RESTFUL_KEY variable with the API key value
- enter your supplier password at least for one Supplier 
- run uvicorn main:app --port 8000 --host 0.0.0.0 --workers 1
- Open http://localhost:8000/ in your browser