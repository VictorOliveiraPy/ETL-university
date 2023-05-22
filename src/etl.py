import pandas as pd
from sqlalchemy import create_engine

from src.config import config
from src.domain.entities.university import University
from src.infrastructure.api_client import get_data_from_api, logger


class ETL:
    """
    Python Extract Transform Load Example
    """

    def __init__(self):
        self.url = config.API_URL

    def extract(self) -> dict:
        logger.info("Extract-Data - Starting data extraction")
        response = get_data_from_api(self.url)
        logger.info("Extract-Data - Extraction completed: %s" % response)
        return response

    def transform(self) -> list[University]:
        logger.info("Transform-Data - Starting data transformation")
        universities = []

        data = self.extract()
        df = pd.DataFrame(data)

        logger.info(f"Total Number of universities from API {len(data)}")
        df[df["name"].str.contains("California")]

        for _, row in df.iterrows():
            university_data = {
                "domains": ",".join(row["domains"]),
                "country": row["country"],
                "web_pages": ",".join(row["web_pages"]),
                "name": row["name"],
            }
            university = University(**university_data)
            universities.append(university)

            df = df.reset_index(drop=True)

        logger.info("Transform-Data - Transformation completed")
        return universities

    def load_data(self) -> None:
        universities_data = self.transform()
        df = pd.DataFrame(universities_data)

        disk_engine = create_engine("sqlite:///my_lite_store.db")
        df.to_sql("cal_uni", disk_engine, if_exists="replace")
        logger.info("Load-Data - Data loaded into SQLite")
