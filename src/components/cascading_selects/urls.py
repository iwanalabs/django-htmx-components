from django.urls import path

from src.components.cascading_selects.select import SelectCascadingSelectsComponent


urlpatterns = [
    path(
        "models/",
        SelectCascadingSelectsComponent.as_view(),
        name="select_cascading_selects",
    ),
]
