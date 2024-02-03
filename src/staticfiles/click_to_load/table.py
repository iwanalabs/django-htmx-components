from django.core.paginator import Paginator
from django_components import component

from app.models import Contact


@component.register("table_click_to_load")
class TableClickToLoadComponent(component.Component):
    template = """
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
                {% component "tbody_click_to_load" page_obj=page_obj only %}
            </tbody>
        </table>
    """

    def get_context_data(self, **kwargs):
        paginator = Paginator(Contact.objects.order_by("id"), 3)
        page_obj = paginator.get_page(1)
        return {"page_obj": page_obj}
