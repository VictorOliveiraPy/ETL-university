import logging
import pandas as pd
from src.repository.university_repository import UniversityRepository

from src.domain.entities.university import University
from src.log import configure_loggng
from src.infrastructure.api_client import api_client
from src.config import config

configure_loggng()

logger = logging.getLogger(__name__)


class UniversityUser:
    def __init__(self):
        self.api_client = config.API_URL
        self.university_repository = UniversityRepository()

    def get_universities(self) -> None:
        data = api_client(self.api_client)
        return self.transform_data(data)

    def create_university_data(self, row):
        university_data = {
            "domains": ",".join(row["domains"]),
            "country": row["country"],
            "web_pages": ",".join(row["web_pages"]),
            "name": row["name"],
        }
        return university_data

    def transform_data(self, data: dict, universities=[]) -> None:
        logger.info("Transform-Data - Starting data transformation")

        df = pd.DataFrame(data)
        df[df["name"].str.contains("California")]

        for _, row in df.iterrows():
            university_data = self.create_university_data(row)
            university = University(**university_data)
            universities.append(university)

        df = df.reset_index(drop=True)

        logger.info("Transform-Data - Transformation completed")
        return self.load_universities(universities)

    def load_universities(self, universities):
        self.university_repository.save_universities(universities)
        logger.info("Load-Universities - Universities loaded")
