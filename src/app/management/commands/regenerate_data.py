from django.core.management.base import BaseCommand
from app.utils import create_contacts, create_brands_and_cars, delete_contacts


class Command(BaseCommand):
    help = "Deletes old data and regenerates new data"

    def handle(self, *args, **kwargs):
        delete_contacts()

        create_contacts(count=100)
        create_brands_and_cars()

        self.stdout.write(self.style.SUCCESS("Successfully regenerated data"))
