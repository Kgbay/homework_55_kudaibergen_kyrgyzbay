from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from task_app.models import Task

from task_app.models import StatusChoice


def add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'task_create.html', context={'choices': StatusChoice.choices})
    task_data = {
        'title': request.POST.get('title'),
        'full_desc': request.POST.get('full_desc'),
        'status': request.POST.get('status'),
        'custom_date': request.POST.get('custom_date'),
        'author': request.POST.get('author')
    }
    task = Task.objects.create(**task_data)
    return redirect('detail_view', pk=task.pk)


def detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task.html', context={
        'task': task
    })


def remove_view(request, pk):
    task_pk = request.GET.get('pk')
    task = Task.objects.get(pk=pk)
    context = {'task': task}
    removal = task.delete()
    return render(request, 'remove.html', context=context)
