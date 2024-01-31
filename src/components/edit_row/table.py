from django.http import HttpResponse
from django_components import component

from src.app.models import Contact


@component.register("table_edit_row")
class TableEditRowComponent(component.Component):
    template = """
        <table class="table">
            <thead class="thead">
                <tr>
                    <th scope="col" class="px-6 py-3">First name</th>
                    <th scope="col" class="px-6 py-3">Last name</th>
                    <th scope="col" class="px-6 py-3">Email</th>
                    <th scope="col" class="px-6 py-3"></th>
                </tr>
            </thead>
            <tbody id="tbody" hx-target="closest tr" hx-swap="outerHTML">
                {% for contact in contacts %}
                    {% component "row_edit_row" contact=contact only %}
                {% endfor %}
            </tbody>
        </table>
    """

    def delete(self, request, id, *args, **kwargs):
        delete_id = int(id)
        Contact.objects.filter(id=delete_id).delete()
        return HttpResponse(status=200)

    def get_context_data(self, **kwargs):
        return {"contacts": Contact.objects.all().order_by("id")[:5]}
