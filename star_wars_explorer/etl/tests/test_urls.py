from django.urls import resolve, reverse


def test_home():
    assert reverse("etl:home") == "/"
    assert resolve("/").view_name == "etl:home"
