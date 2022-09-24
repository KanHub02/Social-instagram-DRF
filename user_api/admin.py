from django.contrib import admin
from .models import User, Followers


admin.site.register(User)
admin.site.register(Followers)

# Register your models here.
