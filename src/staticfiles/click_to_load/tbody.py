from django.core.paginator import Paginator
from django_components import component

from app.models import Contact


@component.register("tbody_click_to_load")
class TBodyClickToLoadComponent(component.Component):
    template = """
        {% for contact in page_obj %}
            <tr class="tr"> 
                <td class="td">{{ contact.id }}</td>
                <td class="td">{{ contact.first_name }} {{ contact.last_name }}</td>
                <td class="td">{{ contact.email }}</td>
                <td class="td">{{ contact.status }}</td>
            </tr>
            {% if forloop.last and page_obj.has_next %} 
                <tr id="replaceMe">
                    <td colspan="4" class="td-tight text-center">
                        <button 
                            class='btn-primary' 
                            hx-get="{% url 'tbody_click_to_load' page=page_obj.next_page_number %}"
                            hx-target="#replaceMe"
                            hx-swap="outerHTML"
                            preload>
                            Load more
                        </button>
                    </td>
                </tr>
            {% endif %}
        {% endfor %}
    """

    def get_context_data(self, page_obj, **kwargs):
        return {"page_obj": page_obj}

    def get(self, request, page, **kwargs):
        paginator = Paginator(Contact.objects.order_by("id"), 3)
        page_obj = paginator.get_page(page)
        context = {"page_obj": page_obj}
        return self.render_to_response(context)
