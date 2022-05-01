from typing import Any

import petl
from django.conf import settings
from django.views.generic import DetailView, ListView

from star_wars_explorer.etl.models import Collection


class CollectionListView(ListView):
    model = Collection
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
