from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from task_app.models import Task

# index view
def index_view(request: WSGIRequest):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context=context)