

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "phone_number",'role',"is_staff",)
    list_filter = ("role",)

admin.site.register(User,CustomUserAdmin)