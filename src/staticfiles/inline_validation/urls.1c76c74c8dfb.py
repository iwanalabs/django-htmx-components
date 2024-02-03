from django.urls import path

from components.inline_validation.form import FormInlineValidationComponent

urlpatterns = [
    path(
        "",
        FormInlineValidationComponent.as_view(),
        name="form_inline_validation",
    ),
]
