import os

from django.core.wsgi import get_wsgi_application
from django.db.backends.signals import connection_created
from django.dispatch import receiver

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()


@receiver(connection_created)
def setup_sqlite(connection, **kwargs):
    if connection.vendor != "sqlite":
        return

    with connection.cursor() as cursor:
        cursor.execute("pragma journal_mode = WAL;")
        cursor.execute("pragma synchronous = NORMAL;")
        cursor.execute("PRAGMA busy_timeout = 10000;")
        cursor.execute("pragma temp_store = memory;")
        cursor.execute("pragma mmap_size = 256000000;")
