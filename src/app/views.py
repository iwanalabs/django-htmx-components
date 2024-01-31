from django.shortcuts import redirect, render, resolve_url

from src.app.models import Contact
from src.app.utils import create_contacts, source_link


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
    files = [
        {
            "name": "components/inline_validation/form.py",
            "path": "inline_validation/form.py",
        },
        {
            "name": "components/inline_validation/forms.py",
            "path": "inline_validation/forms.py",
        },
        {
            "name": "components/inline_validation/input.py",
            "path": "inline_validation/input.py",
        },
        {
            "name": "components/urls.py",
            "path": "inline_validation/urls.py",
        },
        {"name": "template/inline_validation.html", "path": "inline_validation.html"},
    ]
    return render(
        request,
        "inline_validation.html",
        {
            "files": files,
            "title": "Inline Validation",
            "description": "Inline validation of a Django form",
            "full_code_url": source_link("components/inline_validation"),
        },
    )


def bulk_update(request):
    create_contacts(count=3)
    return render(request, "bulk_update.html", {"contacts": Contact.objects.all()})


def click_to_load(request):
    create_contacts()
    files = [
        {"name": "components/click_to_load/table.py", "path": "click_to_load/table.py"},
        {"name": "components/click_to_load/tbody.py", "path": "click_to_load/tbody.py"},
        {"name": "components/click_to_load/urls.py", "path": "click_to_load/urls.py"},
        {"name": "template/click_to_load.html", "path": "click_to_load.html"},
    ]

    return render(
        request,
        "click_to_load.html",
        {
            "files": files,
            "title": "Click to Load",
            "description": "Click to load more data",
            "full_code_url": source_link("components/click_to_load"),
        },
    )


def edit_row(request):
    create_contacts()
    files = [
        {"name": "components/edit_row/row.py", "path": "edit_row/row.py"},
        {"name": "components/edit_row/table.py", "path": "edit_row/table.py"},
        {"name": "components/edit_row/urls.py", "path": "edit_row/urls.py"},
        {"name": "template/edit_row.html", "path": "edit_row.html"},
    ]
    return render(
        request,
        "edit_row.html",
        {
            "files": files,
            "title": "Edit Row",
            "description": "Inline editing of a Django model",
            "full_code_url": source_link("components/edit_row"),
        },
    )


def delete_row(request):
    create_contacts()
    files = [
        {"name": "components/delete_row.py", "path": "delete_row.py"},
        {"name": "components/urls.py", "path": "urls.py", "lines": [10, 14]},
        {"name": "template/delete_row.html", "path": "delete_row.html"},
    ]

    return render(
        request,
        "delete_row.html",
        {
            "files": files,
            "title": "Delete Row",
            "description": "Inline editing of a Django model",
            "full_code_url": source_link("components/delete_row.py"),
        },
    )


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
            "full_code_url": source_link("components/click_to_edit.py"),
        },
    )


def favicon(request):
    return redirect("/static/favicon.ico", permanent=True)
