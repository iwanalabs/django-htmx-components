from django_components import component

from app.models import Contact


@component.register("tbody_active_search")
class TBodyActiveSearchComponent(component.Component):
    template = """
        {% for contact in contacts %}
            <tr class="tr"> 
                <td class="td">{{ contact.first_name }}</td>
                <td class="td">{{ contact.last_name }}</td>
                <td class="td">{{ contact.email }}</td>
                <td class="td">{{ contact.status }}</td>
            </tr>
        {% endfor %}
    """

    def post(self, request, **kwargs):
        search = request.POST.get("search")
        if not search:
            return self.render_to_response({})
        contacts = Contact.objects.filter(
            first_name__icontains=search
        ) | Contact.objects.filter(last_name__icontains=search)
        context = {"contacts": contacts.order_by("id")[:10]}
        return self.render_to_response(context)
