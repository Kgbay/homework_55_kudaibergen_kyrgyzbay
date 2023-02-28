from django.contrib import admin

from .models import Task


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_desc', 'author', 'created_at')
    list_filter = ('id', 'full_desc', 'author', 'created_at')
    search_fields = ('full_desc', 'author')
    fields = ('status', 'full_desc', 'author', 'created_at')
    readonly_fields = ('id', 'created_at', 'updated_at')

admin.site.register(Task, TaskAdmin)