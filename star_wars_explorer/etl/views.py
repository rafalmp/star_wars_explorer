from typing import Any

import petl
from django.conf import settings
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import DetailView, ListView

from star_wars_explorer.etl.etl import transform_and_load
from star_wars_explorer.etl.models import Collection


class CollectionListView(ListView):
    model = Collection
    ordering = ["-created"]
    template_name = "pages/home.html"


class CollectionDetailView(DetailView):
    model = Collection
    template_name = "pages/collection.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        # https://youtrack.jetbrains.com/issue/PY-37457
        # noinspection PyTypeChecker
        num_lines = int(self.request.GET.get("load", settings.LINES_PER_LOAD))
        table = petl.fromcsv(self.get_object().csv_file.path)
        context["csv_data"] = table.head(num_lines)
        context["load_more"] = num_lines + settings.LINES_PER_LOAD
        return context


def fetch_sw_data(request: HttpRequest) -> HttpResponse:
    transform_and_load()
    return HttpResponseRedirect(reverse("etl:home"))


def count(request: HttpRequest, pk: int) -> HttpResponse:
    collection = get_object_or_404(Collection, pk=pk)
    table = petl.fromcsv(collection.csv_file.path)
    counts = petl.valuecounts(table, request.POST["col1"], request.POST["col2"])
    csv_data = petl.head(petl.cutout(counts, "frequency"), settings.LINES_PER_LOAD)
    context = {"collection": collection, "csv_data": csv_data}
    return render(request, "pages/count.html", context=context)
