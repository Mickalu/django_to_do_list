from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from ..models import Task

class TaskForm(ModelForm):
    
    class Meta:
        model = Task
        fields = ('name', 'description',)

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs = {
            'id': 'task-text',
            'placeholder': 'Task Name',
        }
        self.fields['name'].required = True
        self.fields['name'].label = ''


        self.fields['description'].widget.attrs = {
            'id': 'task-description',
            'placeholder': "Description",
        }
        self.fields['description'].label = ''