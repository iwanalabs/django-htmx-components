from django.urls import path

from src.components.infinite_scroll.tbody import TBodyInfiniteScrollComponent

urlpatterns = [
    path(
        "contacts/<int:page>",
        TBodyInfiniteScrollComponent.as_view(),
        name="tbody_infinite_scroll",
    ),
]
