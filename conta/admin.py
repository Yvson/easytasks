from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profile


UserAdmin.list_display = ('username', 'email', 'first_name', 'last_name', 'date_joined', 'is_staff', 'is_active')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']