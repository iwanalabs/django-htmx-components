from django_components import component

from app.models import CarModel


@component.register("select_cascading_selects")
class SelectCascadingSelectsComponent(component.Component):
    template = """
        {% for model in models %}
            <option value="{{ model.id }}">{{ model.name }}</option>
        {% endfor %}
    """

    def get_context_data(self, brand, *args, **kwargs):
        models = CarModel.objects.filter(brand=brand).order_by("name")
        return {"models": models}

    def get(self, request, *args, **kwargs):
        brand = request.GET.get("brand")
        models = CarModel.objects.filter(brand=brand).order_by("name")
        return self.render_to_response({"models": models})
