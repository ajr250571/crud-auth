from tkinter import Widget
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ("title", "description", "important",)
        Widget = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write a Title', }),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a Description', }),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input', }),
        }
