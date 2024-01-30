from django.urls import include, path
from src.components.click_to_edit import ClickToEditComponent
from src.components.delete_row import DeleteRowComponent

urlpatterns = [
    path("click_to_load/", include("src.components.click_to_load.urls")),
    path("bulk_update/", include("src.components.bulk_update.urls")),
    path("inline_validation/", include("src.components.inline_validation.urls")),
    path("edit_row/", include("src.components.edit_row.urls")),
    path(
        "delete_row/contact/<int:id>",
        DeleteRowComponent.as_view(),
        name="contact_delete_row",
    ),
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
]
