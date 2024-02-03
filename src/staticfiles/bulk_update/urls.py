from django.urls import path

from components.bulk_update.tbody import TBodyBulkUpdateComponent

urlpatterns = [
    path(
        "contacts/<str:update>",
        TBodyBulkUpdateComponent.as_view(),
        name="contacts_bulk_update",
    ),
]
