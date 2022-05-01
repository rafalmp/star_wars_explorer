from typing import Optional

import petl.io
import requests


def fetch_page(url: str) -> dict:
    response = requests.get(url)
    return response.json()


def parse_page(page: dict) -> tuple[dict, Optional[str]]:
    return page["results"], page["next"]


def create_data_csv(url: str, header: list, file_path: str) -> None:
    results, next_ = parse_page(fetch_page(url))
    # Define header explicitly as otherwise the column order is not guaranteed when loading data from dicts.
    table = petl.io.fromdicts(results, header=header)
    petl.io.tocsv(table, source=file_path)

    while next_:
        results, next_ = parse_page(fetch_page(next_))
        table = petl.io.fromdicts(results, header=header)
        petl.io.appendcsv(table, source=file_path)
