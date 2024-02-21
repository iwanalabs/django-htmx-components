from django_components import component

from app.models import Contact


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
            <form hx-post="{% url 'contact' id=id %}" hx-target="this" hx-swap="outerHTML" class="form">
                <div class="mb-5">
                    <label class="label" >First Name</label>
                    <input class="input" type="text" name="firstName" value="{{ first_name }}">
                </div>
                <div class="mb-5">
                    <label class="label">Last Name</label>
                    <input class="input" type="text" name="lastName" value="{{ last_name }}">
                </div>
                <div class="mb-5">
                    <label class="label">Email Address</label>
                    <input class="input" type="email" name="email" value="{{ email }}">
                </div>
                <div>
                    <button class="btn-primary">Submit</button>
                    <button class="btn-secondary" hx-get="{% url 'contact' id=id %}">
                        Cancel
                    </button>
                </div>
            </form>
        {% else %}
        <div hx-target="this" hx-swap="outerHTML" class="form">
            <div class="mb-5">
                <label class="label" >First Name</label>
                <input class="disabled-input" type="text" value="{{ first_name }}" disabled>
            </div>
            <div class="mb-5">
                <label class="label">Last Name</label>
                <input class="disabled-input" type="text" value="{{ last_name }}" disabled>
            </div>
            <div class="mb-5">
                <label class="label">Email Address</label>
                <input class="disabled-input" type="email" value="{{ email }}" disabled>
            </div>
            <button class="btn-primary" hx-get="{% url 'contact_edit' id=id %}" preload>Edit contact</button>
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
