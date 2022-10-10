from curses.ascii import US
from django.core.management.base import BaseCommand
import secrets
from media_api.models import Post
from user_api.models import User
import random

RANDOM_STRING_CHARS = "123456789"


def get_random_string(length=5, allowed_chars=RANDOM_STRING_CHARS):

    return "".join(secrets.choice(allowed_chars) for i in range(length))


class Command(BaseCommand):
    help = "Create random posts"

    def handle(self, *args, **kwargs):
        total = 10
        for i in range(total):
            Post.objects.create(
                author=random.choice(User.objects.all()),
                image="medial/random_image" + get_random_string() + ".png",
                title="post #" + get_random_string(),
                description="random description #" + get_random_string(),
                tag="#test",
            )
