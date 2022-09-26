from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    """Model definition for Task."""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Task."""

        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        """Unicode representation of Task."""
        return self.title + ' - por (' + self.user.username + ')'
