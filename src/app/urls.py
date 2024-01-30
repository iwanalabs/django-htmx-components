from django.urls import path

from src.app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("bulk_update/", views.bulk_update, name="bulk_update"),
    path("click_to_edit/", views.click_to_edit, name="click_to_edit"),
    path("click_to_load/", views.click_to_load, name="click_to_load"),
    path("delete_row/", views.delete_row, name="delete_row"),
    path("edit_row/", views.edit_row, name="edit_row"),
    path("inline_validation/", views.inline_validation, name="inline_validation"),
]
