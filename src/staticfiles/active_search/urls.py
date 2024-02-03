from django.urls import path

from components.active_search.tbody import TBodyActiveSearchComponent

urlpatterns = [
    path(
        "search/",
        TBodyActiveSearchComponent.as_view(),
        name="tbody_active_search",
    ),
]
