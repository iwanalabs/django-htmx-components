from django.core.paginator import Paginator
from django_components import component

from src.app.models import Contact


@component.register("table_infinite_scroll")
class TableInfiniteScrollComponent(component.Component):
    template = """
        {% load static %}
        <table class="table">
            <thead class="thead">
                <tr>
                    <th></th>
                    <th class="td">Name</th>
                    <th class="td">Email</th>
                    <th class="td">Status</th>
                </tr>
            </thead>
            <tbody id="tbody">
                {% component "tbody_infinite_scroll" page_obj=page_obj only %}
            </tbody>
        </table>
        <img id="busy-indicator"
             width="24"
             height="24"
             src="{% static 'spinner.svg' %}" class="mt-2"/>
    """

    def get_context_data(self, **kwargs):
        paginator = Paginator(Contact.objects.order_by("id"), 5)
        page_obj = paginator.get_page(1)
        return {"page_obj": page_obj}
