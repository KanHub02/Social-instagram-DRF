from datetime import timedelta
from doctest import FAIL_FAST
from pyexpat import model
from statistics import mode

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import ASCIIUsernameValidator
from .validators import phone_regex
from .managers import UserManager

from social_net.settings import AUTH_USER_MODEL

username_validator = ASCIIUsernameValidator()


class OnlineUserActivity(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    last_activity = models.DateTimeField()

    @staticmethod
    def update_user_activity(user):
        OnlineUserActivity.objects.update_or_create(
            user=user, defaults={"last_activity": timezone.now()}
        )

    @staticmethod
    def get_user_activities(time_delta=timedelta(minutes=15)):
        starting_time = timezone.now() - time_delta
        return OnlineUserActivity.objects.filter(
            last_activity__gte=starting_time
        ).order_by("-last_activity")

    def __str__(self):
        return f"{self.user.username} was online per {self.last_activity}"


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=35, validators=[username_validator], unique=True
    )
    email = models.EmailField(max_length=255, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_private = models.BooleanField(default=False)

    # Profile fields

    user_to = models.ForeignKey(
        "self",
        related_name="to",
        on_delete=models.CASCADE,
        verbose_name="To",
        null=True,
        blank=True,
    )
    user_from = models.ForeignKey(
        "self",
        related_name="by",
        on_delete=models.CASCADE,
        verbose_name="By",
        null=True,
        blank=True,
    )

    user_avatar = models.ImageField(
        default="media/default_avatar.png",
        upload_to="media/uploaded_media/",
        blank=True,
    )
    about_me = models.CharField(max_length=255, blank=True, null=True)
    bio = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(
        validators=[phone_regex], unique=True, blank=True, null=True, max_length=12
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=~models.Q(user_from=models.F("user_to")),
                name="User cant follow to self",
            ),
        ]


# Create your models here.
