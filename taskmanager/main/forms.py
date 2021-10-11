from django.forms import ModelForm, TextInput,Textarea
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'input task'
            }),
            'task' :TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'input text'
            }),
        }