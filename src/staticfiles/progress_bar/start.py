from django_components import component


@component.register("start_progress_bar")
class StartProgressBar(component.Component):
    template = """
        <div hx-target="this" hx-swap="outerHTML" class="progress-bar-div">
            <h3 class="h3 mb-2">Start background task</h3>
            <button class="btn-primary" hx-post="{% url 'start_progress_bar' %}">    
                Start Job 
            </button>
        </div>
    """
