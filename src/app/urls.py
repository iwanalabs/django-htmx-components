from django.urls import path

from app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("active_search/", views.active_search, name="active_search"),
    path("bulk_update/", views.bulk_update, name="bulk_update"),
    path("cascading_selects/", views.cascading_selects, name="cascading_selects"),
    path("click_to_edit/", views.click_to_edit, name="click_to_edit"),
    path("click_to_load/", views.click_to_load, name="click_to_load"),
    path("delete_row/", views.delete_row, name="delete_row"),
    path("edit_row/", views.edit_row, name="edit_row"),
    path("infinite_scroll/", views.infinite_scroll, name="infinite_scroll"),
    path("inline_validation/", views.inline_validation, name="inline_validation"),
    path("progress_bar/", views.progress_bar, name="progress_bar"),
]
