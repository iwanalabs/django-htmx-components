from django.http import HttpResponse
from django_components import component

from src.app.models import Contact


@component.register("row_edit_row")
class RowEditRowComponent(component.Component):
    template = """
        {% if not editing %}
            <tr class="{% if contact.id in ids %} {{ update }} {% endif %}"> 
                <td>{{ contact.first_name }}</td>
                <td>{{ contact.last_name }}</td>
                <td>{{ contact.email }}</td>
                <td>
                    <button class="secondary" hx-get="{% url 'row_edit_row' id=contact.id %}?edit=True" hx-trigger="edit" onClick="editClick(this)">
                    Edit 
                    </button>
                </td>
            </tr>
        {% else %}
            <tr hx-trigger='cancel' class='editing' hx-get="{% url 'row_edit_row' id=contact.id %}">
                <td><input name='first_name' value='{{ contact.first_name }}'></td>
                <td><input name='last_name' value='{{ contact.last_name }}'></td>
                <td><input name='email' value='{{ contact.email }}'></td>
                <td>
                    <button role="button" class="secondary" hx-get="{% url 'row_edit_row' id=contact.id %}">
                        Cancel
                    </button>
                    <button role="button" hx-post="{% url 'row_edit_row' id=contact.id %}" hx-include="closest tr">
                        Save
                    </button>
                </td>
            </tr>
        {% endif %}
    """

    js = """
        function editClick(e) {
            let editing = document.querySelector(".editing");
            if (editing) {
                let changeRow = confirm(
                    "Hey!  You are already editing a row!  Do you want to cancel that edit and continue?"
                );

                if (changeRow) {
                    htmx.trigger(editing, "cancel");
                } else {
                    return;
                }
                
                htmx.trigger(e, "edit");
            } else {
                htmx.trigger(e, "edit");
            }
        }
    """

    def get(self, request, id, *args, **kwargs):
        editing = request.GET.get("edit", False)
        contact = Contact.objects.get(id=id)
        context = {"contact": contact, "editing": editing}
        return self.render_to_response(context)

    def post(self, request, id, *args, **kwargs):
        contact = Contact.objects.get(id=id)
        contact.first_name = request.POST.get("first_name")
        contact.last_name = request.POST.get("last_name")
        contact.email = request.POST.get("email")
        contact.save()
        return self.render_to_response({"contact": contact, "editing": False})

    def get_context_data(self, contact, **kwargs):
        return {"contact": contact}
