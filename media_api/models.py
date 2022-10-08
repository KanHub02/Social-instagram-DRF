from django.core.validators import RegexValidator
from django.db import models
from user_api.models import User
from user_api.validators import tag_validator


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/uploaded_media/", blank=False)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    tag = models.CharField(max_length=255, validators=[tag_validator], blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.post} commented by {self.author}"


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="like")
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.author} liked {self.post}"


# Create your models here.
