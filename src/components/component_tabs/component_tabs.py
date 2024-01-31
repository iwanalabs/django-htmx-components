from django_components import component


@component.register("component_tabs")
class ComponentTabsComponent(component.Component):
    template_name = "component_tabs/component_tabs.html"

    class Media:
        js = "component_tabs/component_tabs.js"
        css = "component_tabs/component_tabs.css"
