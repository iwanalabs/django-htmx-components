from django.urls import path

from src.components.progress_bar.bar import BarProgressBarComponent
from src.components.progress_bar.status import StatusProgressBarComponent


urlpatterns = [
    path(
        "start/",
        StatusProgressBarComponent.as_view(),
        name="start_progress_bar",
    ),
    path(
        "job/<int:id>/completed",
        StatusProgressBarComponent.as_view(),
        name="completed_progress_bar",
    ),
    path(
        "job/<int:id>/progress",
        BarProgressBarComponent.as_view(),
        name="bar_progress_bar",
    ),
]
