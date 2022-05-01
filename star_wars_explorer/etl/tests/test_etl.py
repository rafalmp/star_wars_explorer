from star_wars_explorer.etl.etl import convert_edited_to_date


def test_convert_isodatetime_to_date_string():
    assert (
        convert_edited_to_date({"edited": "2014-12-20T21:17:50.317000Z"})
        == "2014-12-20"
    )
