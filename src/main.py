import logging

from fastapi import FastAPI

from src.etl import ETL
from src.log import configure_loggng

logger = logging.getLogger(__name__)

app = FastAPI()


configure_loggng()


@app.get("/ping")
async def pong():
    executor = ETL()
    executor.load_data()
    return {"Ping": "POng!"}
