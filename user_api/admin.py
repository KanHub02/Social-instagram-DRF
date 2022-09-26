from django.contrib import admin
from .models import User, OnlineUserActivity


admin.site.register(User)
admin.site.register(OnlineUserActivity)

# Register your models here.
