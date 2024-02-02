from django.core.management.base import BaseCommand
from app.utils import create_contacts, create_brands_and_cars, delete_data


class Command(BaseCommand):
    help = "Deletes old data and regenerates new data"

    def handle(self, *args, **kwargs):
        # Assuming you have functions to delete the old data.
        # delete_old_data()

        # Your data creation logic here
        create_contacts(count=100)
        create_brands_and_cars()

        self.stdout.write(self.style.SUCCESS("Successfully regenerated data"))
