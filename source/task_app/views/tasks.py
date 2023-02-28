from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from task_app.models import Task
from task_app.models import StatusChoice
from task_app.forms import TaskForm


def add_view(request: WSGIRequest):
    if request.method == "GET":
        form = TaskForm()
        return render(request, 'task_create.html',
                      context={'choices': StatusChoice.choices,
                               'form': form
                               })
    form = TaskForm(data=request.POST)
    if not form.is_valid():
        return render(request,
                      'task_create.html',
                      context=
                      {'choices': StatusChoice.choices,
                       'form': form,
                       }
                      )
    else:
        task = Task.objects.create(**form.cleaned_data)
        return redirect('detail_view', pk=task.pk)


def detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task.html', context={
        'task': task
    })


def remove_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_confirm_delete.html', context={'task': task})

def confirm_delete_view():
    pass

def update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(initial={
            'title': task.title,
            'status': task.status,
            'custom_date': task.custom_date,
            'author': task.author,
            'full_desc': task.full_desc
        })
        return render(request, 'task_update.html', context=
        {'form': form, 'task': task})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.title = form.cleaned_data['title']
            task.status = form.cleaned_data['status']
            task.custom_date = form.cleaned_data['custom_date']
            task.author = form.cleaned_data['author']
            task.full_desc = form.cleaned_data['full_desc']
            task.save()
            return redirect('detail_view', pk=task.pk)
        else:
            return render(request, 'task_update.html', context={
                'form': form,
                'task': task
            })
