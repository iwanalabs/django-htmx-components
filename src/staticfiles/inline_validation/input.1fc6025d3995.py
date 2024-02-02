from django_components import component


@component.register("input_inline_validation")
class InputInlineValidationComponent(component.Component):
    template = """
        <div id="{{ widget.attrs.id }}-field"
            hx-select="#{{ widget.attrs.id }}-field"
            hx-post="{{ form_url }}"
            hx-trigger="blur from:#{{ widget.attrs.id }}"
            hx-target="this"
            hx-swap="outerHTML">
            {% if label %}
                <label class="label {% if errors %} text-red-700 dark:text-red-500 {% endif %}" for="{{ widget.attrs.id }}">{{ label }}</label>
            {% endif %}
            {% if not widget.type %}
                <textarea class="{% if errors %} input-error {% else %} input {% endif %}" name="{{ widget.name }}"
                        {% for name, value in widget.attrs.items %}
                            {% if value is not False %}
                            {{ name }}
                            {% if value is not True %}="{{ value|stringformat:'s' }}"{% endif %}
                            {% endif %}
                        {% endfor %}>{% if widget.value != None %}{{ widget.value|stringformat:'s' }}{% endif %}</textarea>
            {% else %}
                <input class="{% if errors %} input-error {% else %} input {% endif %}" type="{{ widget.type }}"
                    name="{{ widget.name }}"
                    {% if widget.value != None %}value="{{ widget.value|stringformat:'s' }}"{% endif %}
                    {% for name, value in widget.attrs.items %}
                            {% if value is not False %}
                            {{ name }}
                            {% if value is not True %}="{{ value|stringformat:'s' }}"{% endif %}
                            {% endif %}
                    {% endfor %} />
            {% endif %}
            {% if errors %}
                <ul> 
                    {% for error in errors %}<li class="text-sm text-red-600 dark:text-red-500">{{ error }}</li>{% endfor %}
                </ul>
            {% endif %}
        </div>
    """
