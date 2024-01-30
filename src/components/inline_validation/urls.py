from django.urls import path

from src.components.inline_validation.form import FormInlineValidationComponent

urlpatterns = [
    path(
        "",
        FormInlineValidationComponent.as_view(),
        name="form_inline_validation",
    ),
]
