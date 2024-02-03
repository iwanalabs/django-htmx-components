from django.urls import path

from components.click_to_load.tbody import TBodyClickToLoadComponent

urlpatterns = [
    path(
        "contacts/<int:page>",
        TBodyClickToLoadComponent.as_view(),
        name="tbody_click_to_load",
    ),
]
