from django import forms
from django.urls import reverse_lazy
from components.inline_validation.input import InputInlineValidationComponent


def htmx_inline_validated_input_widget_factory(base_widget_class):
    class HtmxInlineValidatedInputWidget(base_widget_class):
        def __init__(self, attrs=None, form=None, field_name=None, form_url=None):
            super().__init__(attrs)
            self.form = form
            self.field_name = field_name
            self.form_url = form_url

        def get_context(self, name, value, attrs):
            context = super().get_context(name, value, attrs)
            context["form_url"] = self.form_url

            if self.form and self.field_name:
                context["label"] = self.form.fields[self.field_name].label
                context["errors"] = self.form.errors.get(self.field_name, [])
            return context

        def render(self, name, value, attrs=None, renderer=None):
            context = self.get_context(name, value, attrs)
            return InputInlineValidationComponent().render(context)

    return HtmxInlineValidatedInputWidget


class HtmxFormBase(forms.Form):
    form_url = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

        for name, field in self.fields.items():
            if isinstance(field.widget, (forms.Select, forms.FileInput)):
                continue

            custom_widget = htmx_inline_validated_input_widget_factory(
                type(field.widget)
            )
            field.widget = custom_widget(
                form=self,
                field_name=name,
                attrs=field.widget.attrs,
                form_url=self.form_url,
            )


HtmxValidatedTextInput = htmx_inline_validated_input_widget_factory(forms.TextInput)
HtmxValidatedNumberInput = htmx_inline_validated_input_widget_factory(forms.NumberInput)
HtmxValidatedEmailInput = htmx_inline_validated_input_widget_factory(forms.EmailInput)
HtmxValidatedTextarea = htmx_inline_validated_input_widget_factory(forms.Textarea)


class InlineValidationForm(HtmxFormBase):
    form_url = reverse_lazy("form_inline_validation")
    name = forms.CharField(
        label="Name",
        max_length=100,
        widget=HtmxValidatedTextInput(
            attrs={"placeholder": "John Doe"},
        ),
    )
    email = forms.EmailField(
        label="Email",
        widget=HtmxValidatedEmailInput(attrs={"placeholder": "john@doe.com"}),
    )
    age = forms.IntegerField(
        label="Age",
        min_value=13,
        max_value=120,
        widget=HtmxValidatedNumberInput(
            attrs={"placeholder": "e.g., 25"},
        ),
    )
    message = forms.CharField(
        label="Message",
        max_length=500,
        widget=HtmxValidatedTextarea(
            attrs={"placeholder": "Your message here...", "rows": 3},
        ),
    )
