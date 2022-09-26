from datetime import timedelta

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import ASCIIUsernameValidator
from .validators import phone_regex
from .managers import UserManager

username_validator = ASCIIUsernameValidator()


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=35, validators=[username_validator], unique=True
    )
    email = models.EmailField(max_length=255, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # Profile fields

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


class Followers(models.Model):
    user_to = models.ForeignKey(
        User, related_name="follows", on_delete=models.CASCADE, verbose_name="To"
    )
    user_from = models.ForeignKey(
        User, related_name="followers", on_delete=models.CASCADE, verbose_name="By"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name="Создано"
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Followers"
        verbose_name_plural = "Followers"
        constraints = [
            models.CheckConstraint(
                check=~models.Q(user_from=models.F("user_to")),
                name="check_self_follow",
            )
        ]

    def __str__(self):
        return f"{self.user_from.username} followed to {self.user_to.username}"


class OnlineUserActivity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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


# Create your models here.
