import logging

from fastapi import FastAPI

from src.log import configure_loggng
from src.usecase.university_usecase import UniversityUser

logger = logging.getLogger(__name__)

app = FastAPI()


configure_loggng()


@app.get("/ping")
async def pong():
    university_usecase = UniversityUser()
    university_usecase.get_universities()
    return {"Ping": "POng!"}
