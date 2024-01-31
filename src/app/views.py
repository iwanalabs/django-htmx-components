from django.shortcuts import redirect, render, resolve_url

from src.app.models import Contact
from src.app.utils import create_contacts, source_link


def index(request):
    components = [
        {"name": "Active Search", "url": resolve_url("active_search")},
        {"name": "Bulk Update", "url": resolve_url("bulk_update")},
        {"name": "Click to Edit", "url": resolve_url("click_to_edit")},
        {"name": "Click to Load", "url": resolve_url("click_to_load")},
        {"name": "Delete Row", "url": resolve_url("delete_row")},
        {"name": "Edit Row", "url": resolve_url("edit_row")},
        {"name": "Infinite Scroll", "url": resolve_url("infinite_scroll")},
        {"name": "Inline Validation", "url": resolve_url("inline_validation")},
        {"name": "Progress Bar", "url": resolve_url("progress_bar")},
    ]
    return render(request, "index.html", {"components": components})


def reset_database(request):
    Contact.objects.all().delete()
    create_contacts(count=100)
    # redirect to the same page
    return redirect(request.META.get("HTTP_REFERER"))


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
    files = [
        {"name": "components/bulk_update/table.py", "path": "bulk_update/table.py"},
        {"name": "components/bulk_update/tbody.py", "path": "bulk_update/tbody.py"},
        {"name": "components/bulk_update/urls.py", "path": "bulk_update/urls.py"},
        {"name": "template/bulk_update.html", "path": "bulk_update.html"},
    ]
    return render(
        request,
        "bulk_update.html",
        {
            "files": files,
            "title": "Bulk Update",
            "description": "Bulk update of Django models",
            "full_code_url": source_link("components/bulk_update"),
        },
    )


def click_to_load(request):
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


def infinite_scroll(request):
    files = [
        {
            "name": "components/infinite_scroll/table.py",
            "path": "infinite_scroll/table.py",
        },
        {
            "name": "components/infinite_scroll/tbody.py",
            "path": "infinite_scroll/tbody.py",
        },
        {
            "name": "components/infinite_scroll/urls.py",
            "path": "infinite_scroll/urls.py",
        },
        {"name": "template/infinite_scroll.html", "path": "infinite_scroll.html"},
    ]

    return render(
        request,
        "infinite_scroll.html",
        {
            "files": files,
            "title": "Infinite Scroll",
            "description": "Infinite scroll of a Django model",
            "full_code_url": source_link("components/infinite_scroll"),
        },
    )


def active_search(request):
    files = [
        {"name": "components/active_search/input.py", "path": "active_search/input.py"},
        {"name": "components/active_search/tbody.py", "path": "active_search/tbody.py"},
        {"name": "components/active_search/urls.py", "path": "active_search/urls.py"},
        {"name": "template/active_search.html", "path": "active_search.html"},
    ]
    return render(
        request,
        "active_search.html",
        {
            "files": files,
            "title": "Active Search",
            "description": "Active search of a Django model",
            "full_code_url": source_link("components/active_search"),
        },
    )


def progress_bar(request):
    files = [
        {"name": "components/progress_bar/bar.py", "path": "progress_bar/bar.py"},
        {"name": "components/progress_bar/start.py", "path": "progress_bar/start.py"},
        {"name": "components/progress_bar/status.py", "path": "progress_bar/status.py"},
        {"name": "components/progress_bar/urls.py", "path": "progress_bar/urls.py"},
        {"name": "template/progress_bar.html", "path": "progress_bar.html"},
    ]
    return render(
        request,
        "progress_bar.html",
        {
            "files": files,
            "title": "Progress Bar",
            "description": "Progress bar",
            "full_code_url": source_link("components/progress_bar"),
        },
    )


def favicon(request):
    return redirect("/static/favicon.ico", permanent=True)
