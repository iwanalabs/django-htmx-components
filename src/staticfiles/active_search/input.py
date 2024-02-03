from django_components import component


@component.register("input_active_search")
class InputActiveSearchComponent(component.Component):
    template = """
        <div class="mb-4 w-[256px]">
            <input class="input form-control" type="search" 
                name="search" placeholder="Search for a user" 
                hx-post="{% url 'tbody_active_search' %}" 
                hx-trigger="input changed delay:500ms, search" 
                hx-target="#search-results">
        </div>
        <table class="table">
            <thead class="thead">
                <tr>
                    <th class="th">First Name</th>
                    <th class="th">Last Name</th>
                    <th class="th">Email</th>
                    <th class="th">Status</th>
                </tr>
            </thead>
            <tbody id="search-results">
            </tbody>
        </table>
    """
