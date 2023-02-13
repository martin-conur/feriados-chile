import pandas as pd
import requests

def get_chilean_holidays(year: int) -> pd.DataFrame:
    """
        Gets the holidays for the given year.
            Args:
                year: valid year with format 'YYYY' (as int).  Can't be over the current year.
            Returns: 
                A dataframe with the date, holidays name, holidays type and the holidays law info.
    """
    API_URL = url = f"https://apis.digital.gob.cl/fl/feriados/{str(year)}"
    headers = requests.utils.default_headers()

    headers.update(
        {
            'User-Agent': 'My User Agent 1.0',
        }
    )

    r = requests.get(url, headers=headers)
    return (
        pd.DataFrame(r.json())
    )