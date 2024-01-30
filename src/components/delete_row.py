from django.http import HttpResponse
from django_components import component

from src.app.models import Contact


@component.register("delete_row")
class DeleteRowComponent(component.Component):
    template = """
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody id="tbody" hx-confirm="Are you sure?" hx-target="closest tr" hx-swap="outerHTML">
                {% for contact in contacts %}
                <tr class="{% if contact.id in ids %} {{ update }} {% endif %}"> 
                    <td>{{ contact.first_name }} {{ contact.last_name }}</td>
                    <td>{{ contact.email }}</td>
                    <td>{{ contact.status }}</td>
                    <td>
                        <button class="secondary" hx-delete="{% url 'contact_delete_row' id=contact.id %}">
                        Delete
                        </button>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    """

    css = """
        tr.htmx-swapping td {
        opacity: 0;
        transition: opacity 1s ease-out;
        }
    """

    def delete(self, request, id, *args, **kwargs):
        delete_id = int(id)
        Contact.objects.filter(id=delete_id).delete()
        return HttpResponse(status=200)

    def get_context_data(self, **kwargs):
        return {"contacts": Contact.objects.all().order_by("id")[:5]}
