from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import CustomUser


# Unregistering default Django User and Group
admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """ Registering CustomUser """
    list_display = ['id', 'name', 'email', 'created_at']
    list_display_links = ['name']
    search_fields = ['email']
    ordering = ['-id']
