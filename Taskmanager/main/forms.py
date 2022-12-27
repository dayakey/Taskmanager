from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']

        widgets = {
            'title': TextInput(attrs={
                "placeholder": "please create title for task",
                "class": "form-control"
            }),
            'description': Textarea(attrs={
                "placeholder": "please create desc for task",
                "class": "form-control"
            })
        }