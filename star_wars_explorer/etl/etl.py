import os
import uuid
from datetime import datetime
from tempfile import TemporaryDirectory

import petl
from django.conf import settings
from django.core.files import File

from star_wars_explorer.etl.extract import create_data_csv
from star_wars_explorer.etl.models import Collection


def convert_edited_to_date(record: dict) -> str:
    return datetime.fromisoformat(record["edited"].replace("Z", "")).strftime(
        "%Y-%m-%d"
    )


def transform_and_load() -> None:
    with TemporaryDirectory() as tmpdir:
        characters_file_path = os.path.join(tmpdir, "characters.csv")
        planets_file_path = os.path.join(tmpdir, "planets.csv")
        destination_file_name = f"{uuid.uuid4().hex}.csv"
        destination_file_path = os.path.join(tmpdir, destination_file_name)

        create_data_csv(
            settings.SWAPI_CHARACTERS_URL,
            settings.SWAPI_CHARACTER_HEADERS,
            characters_file_path,
        )
        create_data_csv(
            settings.SWAPI_PLANETS_URL,
            settings.SWAPI_PLANETS_HEADERS,
            planets_file_path,
        )

        characters_table = petl.rename(
            petl.io.fromcsv(characters_file_path), "homeworld", "homeworld_url"
        )
        planets_table = petl.rename(
            petl.io.fromcsv(planets_file_path), "name", "homeworld"
        )

        joined_table = petl.transform.join(
            characters_table, planets_table, lkey="homeworld_url", rkey="url"
        )
        joined_table_with_date = petl.transform.addfield(
            joined_table, "date", convert_edited_to_date
        )
        final_table = petl.cutout(joined_table_with_date, "homeworld_url", "edited")

        petl.io.tocsv(final_table, destination_file_path)
        with open(destination_file_path) as f:
            Collection(csv_file=File(f, name=destination_file_name)).save()
