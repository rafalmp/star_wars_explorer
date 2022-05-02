import csv
from typing import Optional

import petl.io
import requests


def fetch_page(url: str) -> dict:
    response = requests.get(url)
    return response.json()


def parse_page(page: dict) -> tuple[dict, Optional[str]]:
    return page["results"], page["next"]


def create_data_csv(url: str, header: list, file_path: str) -> None:
    with open(file_path, "w", newline="") as f:
        csv.writer(f).writerow(header)

    next_: Optional[str] = url
    while next_:
        results, next_ = parse_page(fetch_page(next_))
        table = petl.io.fromdicts(results, header=header)
        petl.io.appendcsv(table, source=file_path)
