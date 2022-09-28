from django.contrib import admin
from .models import User, OnlineUserActivity, FollowerSystem


admin.site.register(User)
admin.site.register(OnlineUserActivity)
admin.site.register(FollowerSystem)


# Register your models here.
