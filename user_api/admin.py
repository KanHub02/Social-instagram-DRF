from django.contrib import admin
from .models import User, Followers, OnlineUserActivity


admin.site.register(User)
admin.site.register(Followers)
admin.site.register(OnlineUserActivity)

# Register your models here.
