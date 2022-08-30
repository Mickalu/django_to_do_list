from multiprocessing import context
from re import template
from django.shortcuts import render
from .forms.add_task import TaskForm

# Create your views here.
def index(request):
    form_task = TaskForm()

    context = locals()
    template = 'index.html'
    return render(request, template, context)