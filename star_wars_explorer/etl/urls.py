from django.urls import path

from star_wars_explorer.etl.views import (
    CollectionDetailView,
    CollectionListView,
    fetch_sw_data,
)

app_name = "etl"

urlpatterns = [
    path("", CollectionListView.as_view(), name="home"),
    path("<int:pk>/", CollectionDetailView.as_view(), name="details"),
    path("fetch/", fetch_sw_data, name="fetch"),
]
