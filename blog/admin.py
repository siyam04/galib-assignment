from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ Registering Post """
    list_display = ['id', 'title', 'content', 'created_at']
    list_display_links = ['title']
    search_fields = ['title']
    ordering = ['-id']
