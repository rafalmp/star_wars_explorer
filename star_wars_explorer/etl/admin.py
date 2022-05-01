from django.contrib import admin

from star_wars_explorer.etl.models import Collection


class CollectionAdmin(admin.ModelAdmin):
    list_display = ("created",)


admin.site.register(Collection, CollectionAdmin)
