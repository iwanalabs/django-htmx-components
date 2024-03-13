from django.db import migrations
from django.contrib.sites.models import Site


def create_site(apps, schema_editor):
    Site.objects.all().delete()
    Site.objects.create(domain="dhc.iwanalabs.com", name="Iwana Labs")


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_init_data"),
        ("sites", "0002_alter_domain_unique"),
    ]

    operations = [
        migrations.RunPython(create_site),
    ]
