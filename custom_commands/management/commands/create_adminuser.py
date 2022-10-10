from social_net.settings import AUTH_USER_MODEL
from user_api.models import User
from django.core.management.base import BaseCommand
import secrets


class Command(BaseCommand):
    help = "Create random users with username - admin, password - 12345, email - admin@mail.com "

    def handle(self, *args, **kwargs):
        total = 1
        for i in range(total):
            User.objects.create_superuser(
                username="admin",
                email="admin@mail.com",
                password="12345",
            )
