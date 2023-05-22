import logging

import requests
from requests import RequestException, Timeout, TooManyRedirects

from src.log import configure_loggng

configure_loggng()

logger = logging.getLogger(__name__)


def get_data_from_api(api_url: str) -> dict:
    try:
        response = requests.get(api_url).json()
    except (RequestException, Timeout, TooManyRedirects, ConnectionError) as e:
        logger.exception("An exception occurred during the request:", e)
        return

    return response
