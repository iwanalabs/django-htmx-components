from django.shortcuts import redirect, render, resolve_url

from src.app.models import Contact
from src.app.utils import create_contacts


def index(request):
    components = [
        {"name": "Click to Edit", "url": resolve_url("click_to_edit")},
        {"name": "Inline Validation", "url": resolve_url("inline_validation")},
        {"name": "Click to Load", "url": resolve_url("click_to_load")},
        {"name": "Bulk Update", "url": resolve_url("bulk_update")},
        {"name": "Delete Row", "url": resolve_url("delete_row")},
        {"name": "Edit Row", "url": resolve_url("edit_row")},
    ]
    return render(request, "index.html", {"components": components})


def inline_validation(request):
    return render(request, "inline_validation.html")


def bulk_update(request):
    create_contacts(count=3)
    return render(request, "bulk_update.html", {"contacts": Contact.objects.all()})


def click_to_load(request):
    create_contacts()
    return render(request, "click_to_load.html")


def edit_row(request):
    create_contacts()
    return render(request, "edit_row.html")


def delete_row(request):
    create_contacts()
    return render(request, "delete_row.html")


def click_to_edit(request):
    create_contacts(count=1)

    files = [
        {"name": "components/click_to_edit.py", "path": "click_to_edit.py"},
        {"name": "components/urls.py", "path": "urls.py", "lines": [15, 24]},
        {"name": "template/click_to_edit.html", "path": "click_to_edit.html"},
    ]

    return render(
        request,
        "click_to_edit.html",
        {
            "files": files,
            "title": "Click to Edit",
            "description": "Inline editing of a Django model",
            "full_code_url": "https://github.com/iwanalabs/django-htmx-components/blob/main/src/components/click_to_edit.py",
        },
    )


def favicon(request):
    return redirect("/static/favicon.ico", permanent=True)
