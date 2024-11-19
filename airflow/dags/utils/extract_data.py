import pandas as pd
import requests
import numpy as np


def extract_data():
    url = 'https://restcountries.com/v3.1/all'
    response = requests.get(f"{url}")
    df = pd.DataFrame(response.json())
    return df
