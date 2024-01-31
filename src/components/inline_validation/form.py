from django_components import component

from src.components.inline_validation.forms import InlineValidationForm


@component.register("form_inline_validation")
class FormInlineValidationComponent(component.Component):
    template = """
        <form id="inline-validation-form" class="form">
            <div class="mb-5">
                {{ form.name }}
                {{ form.name.type.errors }}
            </div>
            <div class="mb-5">
                {{ form.email }}
                {{ form.email.type.errors }}
            </div>
            <div class="mb-5">
                {{ form.age }}
                {{ form.age.type.errors }}
            </div>
            <div class="mb-5">
                {{ form.message }}
                {{ form.message.type.errors }}
            </div>
        </form>
    """

    def get_context_data(self, **kwargs):
        form = InlineValidationForm()
        return {"form": form}

    def post(self, request, *args, **kwargs):
        form = InlineValidationForm(request.POST)
        return self.render_to_response({"form": form})
