from django.core.management.base import BaseCommand
import secrets
from media_api.models import Post, Like
from user_api.models import User
import random


class Command(BaseCommand):
    help = "Create random Like to posts"

    def add_arguments(self, parser):
        parser.add_argument(
            "total", type=int, help="Indicates the number of users to be created"
        )

    def handle(self, *args, **kwargs):
        total = kwargs["total"]
        for i in range(total):
            Like.objects.create(
                author=random.choice(User.objects.all()),
                post=random.choice(Post.objects.all()),
            )
