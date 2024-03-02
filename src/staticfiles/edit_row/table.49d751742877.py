from django.http import HttpResponse
from django_components import component

from app.models import Contact


@component.register("table_edit_row")
class TableEditRowComponent(component.Component):
    template = """
        <table class="table">
            <thead class="thead">
                <tr>
                    <th scope="col" class="th">First name</th>
                    <th scope="col" class="th">Last name</th>
                    <th scope="col" class="th">Email</th>
                    <th scope="col" class="th"></th>
                </tr>
            </thead>
            <tbody id="tbody" hx-target="closest tr" hx-swap="outerHTML">
                {% for contact in contacts %}
                    {% component "row_edit_row" contact=contact only %}{% endcomponent %}
                {% endfor %}
            </tbody>
        </table>
    """

    def get_context_data(self, **kwargs):
        return {"contacts": Contact.objects.all().order_by("id")[:5]}  # remove limit
