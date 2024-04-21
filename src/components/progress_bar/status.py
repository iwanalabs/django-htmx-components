from typing import Any, Dict
from django_components import component
from app.models import Job


@component.register("status_progress_bar")
class StatusProgressBarComponent(component.Component):
    template = """
        <div class="progress-bar-div" hx-trigger="done" hx-get="{% url 'completed_progress_bar' id=job.id %}" hx-swap="outerHTML" hx-target="this">
            <h3 role="status" id="pblabel" tabindex="-1" autofocus>
                {% if not done %}
                    Running
                {% else %}
                    Complete
                {% endif %}
            </h3>
            {% component "bar_progress_bar" id=job.id done=done %}{% endcomponent %}
        </div>
        {% if done %}
            <button id="restart-btn" class="btn-primary" hx-post="{% url 'start_progress_bar' %}" classes="add show:600ms">
                Restart Job
            </button>
        {% endif %}
    """

    def get(self, request, id, **kwargs):
        job = Job.objects.get(id=id)
        return self.render_to_response({"job": job, "done": True})

    def post(self, request, **kwargs):
        job = Job.objects.create(progress=0)
        return self.render_to_response({"job": job})
