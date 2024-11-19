import pandas as pd
import requests
import numpy as np
from .extract_data import extract_data
import awswrangler as wr
import pandas as pd

def transform_data(df):
    currency_details = df['currencies'].apply(extract_currency_details)
    df = pd.concat([df, currency_details], axis=1)
    
    df['country_name'] = df['name'].apply(lambda x: x.get('common'))
    
    df['official_country_name'] = df['name'].apply(lambda x: x.get('official'))

    df['common_native_names'] = df['name'].apply(lambda x: extract_all_common_native_names(x.get('nativeName')))

    df['languages'] = df['languages'].apply(lambda x: extract_languages(x))

    df['country_code'] = df['idd'].apply(lambda x: generate_country_codes(x))

    df['continents'] = df['continents'].str[0]
    
    df['capital'] = df['capital'].str[0]

    df = df.drop(columns=['name', 'idd', 'currencies'])

    #Desired column order
    desired_order = [
        'country_name', 'independent', 'unMember', 'startOfWeek',
        'official_country_name', 'common_native_names',
        'currency_code', 'currency_name', 'currency_symbol',
        'country_code', 'capital', 'region', 'subregion',
        'languages', 'area', 'population', 'continents'
    ]

    # Reorder columns in the DataFrame
    df = df[desired_order]
    return df



def extract_currency_details(row):
    if isinstance(row, dict) and len(row) > 0:
        valid_entry = {key: value for key, value in row.items() if value is not None}
        if valid_entry:
            code = list(valid_entry.keys())[0]
            details = valid_entry[code]
            return pd.Series({
                'currency_code': code,
                'currency_name': details.get('name', None),
                'currency_symbol': details.get('symbol', None)
            })
    return pd.Series({'currency_code': None, 'currency_name': None, 'currency_symbol': None})


def extract_languages(language):
    if isinstance(language, dict):
        return ", ".join(str(value) for value in language.values() if value is not None)
    return None


def extract_all_common_native_names(native_name):
    if isinstance(native_name, dict):
        return ", ".join(entry.get('common', '') for entry in native_name.values() if isinstance(entry, dict) and 'common' in entry)
    return None


def generate_country_codes(idd):
    if isinstance(idd, dict):
        root = idd.get('root', '')
        suffixes = idd.get('suffixes', [])
        if isinstance(suffixes, (list, np.ndarray)):
            return " ".join([root + suffix for suffix in suffixes])
    return None