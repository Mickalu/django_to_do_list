from multiprocessing import context
from re import template
from django.shortcuts import render
from .forms.add_task import TaskForm

# Create your views here.
def index(request):
    form_task = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task_object = form.save()
            user = request.user
            task_object.user = user
            task_object.save()

    context = locals()
    template = 'index.html'
    return render(request, template, context)