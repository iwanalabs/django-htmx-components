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
                <label for="{{ widget.attrs.id }}">{{ label }}</label>
            {% endif %}
            {% if not widget.type %}
                <textarea name="{{ widget.name }}"
                        {% for name, value in widget.attrs.items %}
                            {% if value is not False %}
                            {{ name }}
                            {% if value is not True %}="{{ value|stringformat:'s' }}"{% endif %}
                            {% endif %}
                        {% endfor %}>{% if widget.value != None %}{{ widget.value|stringformat:'s' }}{% endif %}</textarea>
            {% else %}
                <input type="{{ widget.type }}"
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
                    {% for error in errors %}<li><small>{{ error }}</small></li>{% endfor %}
                </ul>
            {% endif %}
        </div>
    """
