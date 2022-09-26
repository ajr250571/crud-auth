from distutils.command import register
import site
from unittest import suite
from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(Task, TaskAdmin)
