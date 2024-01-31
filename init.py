import os

import django

print("Initializing Django...")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.config.settings")
os.environ[
    "DJANGO_ALLOW_ASYNC_UNSAFE"
] = "true"  # needed for db migrate, possibly other operations
django.setup()

print("Django initialized.")

print("Running migrations...")

from django.core.management.commands.migrate import Command as MigrateCommand

MigrateCommand().handle(
    database="default",
    skip_checks=False,
    verbosity=1,
    interactive=False,
    app_label=None,
    migration_name=None,
    noinput=True,
    fake=False,
    fake_initial=False,
    plan=False,
    run_syncdb=False,
    check=False,
    prune=False,
    check_unapplied=False,
)
print("Migrations complete.")

print("Loading data...")

from django.contrib.auth.models import User

# add a user for accessing the admin
user = User(username="admin", is_staff=True, is_superuser=True)
user.set_password("password")
user.save()
print("Data loaded.")

# set up the app we'll use to serve requests
from django.core.wsgi import get_wsgi_application
from webtest import TestApp
from django.contrib.staticfiles.handlers import StaticFilesHandler


wsgi_application = StaticFilesHandler(get_wsgi_application())
app = TestApp(wsgi_application)
