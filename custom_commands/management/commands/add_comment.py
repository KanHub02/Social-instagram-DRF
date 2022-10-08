from curses.ascii import US
from django.core.management.base import BaseCommand
import secrets
from media_api.models import Post, Comment
from user_api.models import User
import random

RANDOM_STRING_CHARS = "qwertyuiopasdfghjklzxcvbnm"


def get_random_string(length=5, allowed_chars=RANDOM_STRING_CHARS):

    return "".join(secrets.choice(allowed_chars) for i in range(length))


class Command(BaseCommand):
    help = "Create random comments to posts"

    def add_arguments(self, parser):
        parser.add_argument(
            "total", type=int, help="Indicates the number of users to be created"
        )

    def handle(self, *args, **kwargs):
        total = kwargs["total"]
        for i in range(total):
            Comment.objects.create(
                author=random.choice(User.objects.all()),
                text="Wow!" + get_random_string(),
                post=random.choice(Post.objects.all()),
            )
