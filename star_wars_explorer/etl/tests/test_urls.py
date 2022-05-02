from django.urls import resolve, reverse


def test_home():
    assert reverse("etl:home") == "/"
    assert resolve("/").view_name == "etl:home"


def test_details():
    assert reverse("etl:details", kwargs={"pk": 1}) == "/1/"
    assert resolve("/1/").view_name == "etl:details"


def test_fetch():
    assert reverse("etl:fetch") == "/fetch/"
    assert resolve("/fetch/").view_name == "etl:fetch"


def test_count():
    assert reverse("etl:count", kwargs={"pk": 1}) == "/1/count/"
    assert resolve("/1/count/").view_name == "etl:count"
