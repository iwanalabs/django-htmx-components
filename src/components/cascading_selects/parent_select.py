from typing import Any, Dict
from django_components import component

from src.app.models import Brand


@component.register("parent_select_cascading_selects")
class ParentSelectCascadingSelectsComponent(component.Component):
    template = """
        <div>
            <label class="label">Brand</label>
            <select class="input" name="brand" hx-get="{% url 'select_cascading_selects' %}" hx-target="#models">
            {% for brand in brands %}
                <option value="{{ brand.id }}">{{ brand.name }}</option>
            {% endfor %}
            </select>
        </div>
        <div class="mt-2">
            <label class="label">Model</label>
            <select id="models" name="model" class="input">
                {% component "select_cascading_selects" brand=brands.0.id %}
            </select>
        </div>
    """

    def get_context_data(self, *args, **kwargs) -> Dict[str, Any]:
        brands = Brand.objects.order_by("name")
        return {"brands": brands}
