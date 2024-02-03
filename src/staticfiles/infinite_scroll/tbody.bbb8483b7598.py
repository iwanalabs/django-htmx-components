import time
from django.core.paginator import Paginator
from django_components import component

from app.models import Contact


@component.register("tbody_infinite_scroll")
class TBodyInfiniteScrollComponent(component.Component):
    template = """
        {% for contact in page_obj %}
            <tr class="tr"
            {% if forloop.last and page_obj.has_next %} 
                hx-get="{% url 'tbody_infinite_scroll' page=page_obj.next_page_number %}"
                hx-trigger="revealed"
                hx-swap="afterend"
            {% endif %}
            > 
                <td class="td">{{ contact.id }}</td>
                <td class="td">{{ contact.first_name }} {{ contact.last_name }}</td>
                <td class="td">{{ contact.email }}</td>
                <td class="td">{{ contact.status }}</td>
            </tr>
        {% endfor %}
    """

    def get_context_data(self, page_obj, **kwargs):
        return {"page_obj": page_obj}

    def get(self, request, page, **kwargs):
        paginator = Paginator(Contact.objects.order_by("id"), 10)
        time.sleep(1)  # Simulate a slow response
        page_obj = paginator.get_page(page)
        context = {"page_obj": page_obj}
        return self.render_to_response(context)
