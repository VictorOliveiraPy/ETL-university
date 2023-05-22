import logging
import pandas as pd
from sqlalchemy import create_engine

from src.log import configure_loggng


configure_loggng()

logger = logging.getLogger(__name__)


class UniversityRepository:
    def __init__(self) -> None:
        self.disk_engine = create_engine("sqlite:///my_lite_store.db")
        
    
    def save_universities(self, universities):
        try:
            df = pd.DataFrame(universities)
            df.to_sql("cal_uni", self.disk_engine, if_exists="replace")
            logger.info("Data loaded into SQLite")
        except pd.errors.DatabaseError as e:
             logger.error("Error occurred while creating DataFrame: " + str(e))
        except Exception as e:
            logger.error("An error occurred while saving universities: " + str(e))
            
        