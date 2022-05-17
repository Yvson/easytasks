from django.contrib import admin
from .models import Number, Password


@admin.register(Number)
class NumberAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'profile', 'trunc_numbers']

    @admin.display(description='Numbers')
    def trunc_numbers(self, obj):
        return obj.numbers[:100] + '...'


@admin.register(Password)
class PasswordAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'profile', 'password']
