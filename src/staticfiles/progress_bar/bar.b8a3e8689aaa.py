from django.http import HttpResponse
from django_components import component
from app.models import Job


@component.register("bar_progress_bar")
class BarProgressBarComponent(component.Component):
    template = """
        <div
            hx-get="{% url 'bar_progress_bar' id=job.id %}"
            {% if not done %}
            hx-trigger="every 600ms"
            {% else %}
            hx-trigger="none"
            {% endif %}
            hx-target="this"
            hx-swap="innerHTML">
            <div class="progress" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="{{ current_progress }}" aria-labelledby="pblabel">
                <div id="pb" class="progress-bar" style="width:{{ current_progress }}%">
            </div>
        </div>
    """

    css = """
        .progress {
            height: 20px;
            margin-bottom: 20px;
            overflow: hidden;
            background-color: #f5f5f5;
            border-radius: 4px;
            box-shadow: inset 0 1px 2px rgba(0,0,0,.1);
        }
        .progress-bar {
            float: left;
            width: 0%;
            height: 100%;
            font-size: 12px;
            line-height: 20px;
            color: #fff;
            text-align: center;
            background-color: rgb(26 86 219);
            -webkit-box-shadow: inset 0 -1px 0 rgba(0,0,0,.15);
            box-shadow: inset 0 -1px 0 rgba(0,0,0,.15);
            -webkit-transition: width .6s ease;
            -o-transition: width .6s ease;
            transition: width .6s ease;
        }
    """

    def get_context_data(self, id, **kwargs):
        job = Job.objects.get(id=id)
        return {"job": job, "current_progress": job.progress}

    def get(self, request, id, **kwargs):
        job = Job.objects.get(id=id)
        job.progress += 10
        job.save()

        context = {
            "job": job,
            "current_progress": job.progress,
        }
        headers = {}

        if job.progress >= 100:
            headers = {"HX-Trigger": "done"}

        return HttpResponse(self.render(context), headers=headers)
