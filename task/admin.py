from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """ Registering Post """
    list_display = ['id', 'title', 'is_completed', 'created_at']
    list_display_links = ['title']
    search_fields = ['title', 'created_at']
    list_editable = ['is_completed']
    ordering = ['-id']
