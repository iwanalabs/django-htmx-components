from django_components import component

from src.app.models import Contact


def build_context(contact, editing=False):
    return {
        "first_name": contact.first_name,
        "last_name": contact.last_name,
        "email": contact.email,
        "id": contact.id,
        "editing": editing,
    }


@component.register("click_to_edit")
class ClickToEditComponent(component.Component):
    template = """
        {% if editing %}
            <form hx-post="{% url 'contact' id=id %}" hx-target="this" hx-swap="outerHTML">
            <div>
                <label>First Name</label>
                <input type="text" name="firstName" value="{{ first_name }}">
            </div>
            <div class="form-group">
                <label>Last Name</label>
                <input type="text" name="lastName" value="{{ last_name }}">
            </div>
            <div class="form-group">
                <label>Email Address</label>
                <input type="email" name="email" value="{{ email }}">
            </div>
            <div>
                <button class="primary">Submit</button>
                <button class="secondary" hx-get="{% url 'contact' id=id %}">
                    Cancel
                </button>
            </div>
            </form>
        {% else %}
        <div hx-target="this" hx-swap="outerHTML">
            <div>
                <b>First Name</b>: {{ first_name }}
            </div>
            <div>
                <b>Last Name</b>: {{ last_name }}
            </div>
            <div>
                <b>Email</b>: {{ email }}
            </div>
            <button hx-get="{% url 'contact_edit' id=id %}">Click To Edit</button>
        </div>
        {% endif %}
    """

    def get_context_data(self, id, **kwargs):
        contact = Contact.objects.get(id=id)
        return build_context(contact)

    def get(self, request, id, *args, **kwargs):
        contact = Contact.objects.get(id=id)
        context = build_context(contact, request.path.endswith("edit"))
        return self.render_to_response(context)

    def post(self, request, id, *args, **kwargs):
        contact = Contact.objects.get(id=id)
        contact.first_name = request.POST.get("firstName")
        contact.last_name = request.POST.get("lastName")
        contact.email = request.POST.get("email")
        contact.save()
        context = build_context(contact, request.path.endswith("edit"))
        return self.render_to_response(context)
