from user_api.models import User
from media_api.models import Post
from django.core.management.base import BaseCommand
import secrets


RANDOM_STRING_CHARS = "123456789"


def get_random_string(length=5, allowed_chars=RANDOM_STRING_CHARS):

    return "".join(secrets.choice(allowed_chars) for i in range(length))


class Command(BaseCommand):
    help = "Create random post"

    def add_arguments(self, parser):
        parser.add_argument(
            "total", type=int, help="Indicates the number of users to be created"
        )

    def handle(self, *args, **kwargs):
        total = kwargs["total"]
        for i in range(total):
            Post.objects.create(
                author="testuser" + get_random_string(),
                image="medial/random_image" + get_random_string() + ".png",
                title="post #" + get_random_string(),
                description="random description #" + get_random_string(),
                tag="#test",
            )
