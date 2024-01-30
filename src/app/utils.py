from src.app.models import Contact

contacts_list = [
    {
        "id": 1,
        "first_name": "Joe",
        "last_name": "Blow",
        "email": "joe@blow.com",
        "status": "active",
    },
    {
        "id": 2,
        "first_name": "Jane",
        "last_name": "Doe",
        "email": "jane@doe.com",
        "status": "active",
    },
    {
        "id": 3,
        "first_name": "John",
        "last_name": "Smith",
        "email": "joe@smith.com",
        "status": "active",
    },
    {
        "id": 4,
        "first_name": "Jane",
        "last_name": "Smith",
        "email": "jane@smith.com",
        "status": "active",
    },
    {
        "id": 5,
        "first_name": "John",
        "last_name": "Doe",
        "email": "jonh@doe.com",
        "status": "inactive",
    },
    {
        "id": 6,
        "first_name": "Joe",
        "last_name": "Smith",
        "email": "joe@smith.com",
        "status": "inactive",
    },
    {
        "id": 7,
        "first_name": "Jane",
        "last_name": "Blow",
        "email": "jane@bloe",
        "status": "inactive",
    },
    {
        "id": 8,
        "first_name": "John",
        "last_name": "Taylor",
        "email": "john@taylor.com",
        "status": "inactive",
    },
    {
        "id": 9,
        "first_name": "Jane",
        "last_name": "Taylor",
        "email": "jane@taylor.com",
        "status": "inactive",
    },
    {
        "id": 10,
        "first_name": "John",
        "last_name": "Roberts",
        "email": "john@roberts",
        "status": "inactive",
    },
]


def create_contacts(contacts=contacts_list, count=None):
    for contact in contacts[:count]:
        Contact.objects.get_or_create(
            id=contact["id"],
            defaults={
                "first_name": contact["first_name"],
                "last_name": contact["last_name"],
                "email": contact["email"],
                "status": contact["status"],
            },
        )
