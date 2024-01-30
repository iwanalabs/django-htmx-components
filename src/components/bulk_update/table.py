from django_components import component

from django.middleware.csrf import get_token

from src.app.models import Contact


@component.register("table_bulk_update")
class TableBulkUpdateComponent(component.Component):
    template = """
        <div hx-include="#checked-contacts" hx-target="#tbody">
            <button class="primary"
                    hx-post="{% url 'contacts_bulk_update' update='activate' %}">Activate</button>
            <button class="secondary"
                    hx-post="{% url 'contacts_bulk_update' update='deactivate' %}">Deactivate</button>
        </div>
        <form id="checked-contacts">
            <table>
                <thead>
                    <tr>
                        <th></th>
                        <th>Name</th>
                        <th>Email</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody id="tbody">
                    {% component "tbody_bulk_update" contacts=contacts only %}
                </tbody>
            </table>
        </form>
    """

    css = """
        .htmx-settling tr.deactivate td {
            background: lightcoral;
        }
        .htmx-settling tr.activate td {
            background: darkseagreen;
        }
        tr td {
            transition: all 1.2s;
        }
    """

    def get_context_data(self, **kwargs):
        return {"contacts": Contact.objects.all()}

    def get(self, request, *args, **kwargs):
        return self.render_to_response(
            {
                "contacts": Contact.objects.all(),
                "csrf_token": get_token(request),
            }
        )
