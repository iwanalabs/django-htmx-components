from django_components import component

from src.app.models import Contact


@component.register("tbody_bulk_update")
class TBodyBulkUpdateComponent(component.Component):
    template = """
        {% for contact in contacts %}
        <tr class="{% if contact.id in ids %} {{ update }} {% endif %}"> 
            <td><input type='checkbox' name='ids' value='{{ contact.id }}'></td>
            <td>{{ contact.first_name }} {{ contact.last_name }}</td>
            <td>{{ contact.email }}</td>
            <td>{{ contact.status }}</td>
        </tr>
        {% endfor %}
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

    def get_context_data(self, contacts, **kwargs):
        return {"contacts": contacts}

    def post(self, request, update, *args, **kwargs):
        if update == "activate":
            Contact.objects.filter(id__in=request.POST.getlist("ids")).update(
                status="Active"
            )
        elif update == "deactivate":
            Contact.objects.filter(id__in=request.POST.getlist("ids")).update(
                status="Inactive"
            )
        context = {
            "contacts": Contact.objects.all(),
            "update": update,
            "ids": [int(id_) for id_ in request.POST.getlist("ids")],
        }
        return self.render_to_response(context)
