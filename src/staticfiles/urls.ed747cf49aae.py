from django.urls import include, path
from components.click_to_edit import ClickToEditComponent
from components.delete_row import DeleteRowComponent

urlpatterns = [
    path("active_search/", include("components.active_search.urls")),
    path("bulk_update/", include("components.bulk_update.urls")),
    path("cascading_selects/", include("components.cascading_selects.urls")),
    path(
        "click_to_edit/contact/<int:id>",
        ClickToEditComponent.as_view(),
        name="contact",
    ),
    path(
        "click_to_edit/contact/<int:id>/edit",
        ClickToEditComponent.as_view(),
        name="contact_edit",
    ),
    path("click_to_load/", include("components.click_to_load.urls")),
    path(
        "delete_row/contact/<int:id>",
        DeleteRowComponent.as_view(),
        name="contact_delete_row",
    ),
    path("edit_row/", include("components.edit_row.urls")),
    path("infinite_scroll/", include("components.infinite_scroll.urls")),
    path("inline_validation/", include("components.inline_validation.urls")),
    path("progress_bar/", include("components.progress_bar.urls")),
]
