from social_net.settings import AUTH_USER_MODEL
from user_api.models import User
from django.core.management.base import BaseCommand
import secrets


RANDOM_STRING_CHARS = "123456789"


def get_random_string(length=5, allowed_chars=RANDOM_STRING_CHARS):

    return "".join(secrets.choice(allowed_chars) for i in range(length))


class Command(BaseCommand):
    help = "Create random users"

    def add_arguments(self, parser):
        parser.add_argument(
            "total", type=int, help="Indicates the number of users to be created"
        )

    def handle(self, *args, **kwargs):
        total = kwargs["total"]
        for i in range(total):
            User.objects.create_user(
                username="testuser" + get_random_string(),
                email=get_random_string() + "@mail.com",
                password="kanat2002",
            )
