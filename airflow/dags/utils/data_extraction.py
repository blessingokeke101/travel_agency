import logging

import pandas as pd
import requests


def extract_api_data():
    """
    Retrieves data from a predefined API endpoint and
    converts it into a Pandas DataFrame.

    Returns:
        pd.DataFrame -> A DataFrame containing the retrieved data from the API.

    Raises:
        requests.exceptions.RequestException
        If an error occurs during the API request, such as a network issue or
          an invalid response.
    """
    try:
        url = 'https://restcountries.com/v3.1/all'
        response = requests.get(f"{url}")
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching user profiles: {e}")

    df = pd.DataFrame(response.json())
    return df
