import csv

from star_wars_explorer.etl.extract import create_data_csv, fetch_page, parse_page


def test_fetch_page(mocked_responses):
    mocked_responses.get("https://example.com", json={"test": "value"})
    assert fetch_page("https://example.com") == {"test": "value"}


def test_parse_page():
    assert parse_page(
        {"next": "https://example.com", "results": [{"test": "value"}]}
    ) == ([{"test": "value"}], "https://example.com")


def test_create_data_csv(mocked_responses, tmp_path):
    mocked_responses.get(
        "https://example.com",
        json={
            "next": "https://example.com?page=2",
            "results": [{"col1": "val1", "col2": "val2"}],
        },
    )
    mocked_responses.get(
        "https://example.com?page=2",
        json={
            "next": None,
            "results": [{"col1": "val3", "col2": "val4"}],
        },
    )
    tmp_csv = tmp_path / "test.csv"
    create_data_csv("https://example.com", ["col1"], str(tmp_csv))
    with open(tmp_csv, newline="") as fp:
        assert list(csv.reader(fp)) == [["col1"], ["val1"], ["val3"]]
