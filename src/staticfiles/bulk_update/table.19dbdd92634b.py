from django_components import component

from django.middleware.csrf import get_token

from app.models import Contact


@component.register("table_bulk_update")
class TableBulkUpdateComponent(component.Component):
    template = """
        <form id="checked-contacts">
            <table class="table">
                <thead class="thead">
                    <tr>
                        <th class="th"></th>
                        <th class="th">Name</th>
                        <th class="th">Email</th>
                        <th class="th">Status</th>
                    </tr>
                </thead>
                <tbody id="tbody">
                    {% component "tbody_bulk_update" contacts=contacts only %}{% endcomponent %}
                </tbody>
            </table>
        </form>
        <div class="mt-4" hx-include="#checked-contacts" hx-target="#tbody">
            <button class="btn-primary"
                    hx-post="{% url 'contacts_bulk_update' update='activate' %}">Activate</button>
            <button class="btn-secondary"
                    hx-post="{% url 'contacts_bulk_update' update='deactivate' %}">Deactivate</button>
        </div>
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
        return {"contacts": Contact.objects.all().order_by("id")[:5]}  # remove limit
