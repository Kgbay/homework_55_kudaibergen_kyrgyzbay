from django.urls import path

from .views.base import index_view
from .views.tasks import add_view, detail_view, remove_view

urlpatterns = [
    path("", index_view, name='index'),
    path("task/add/", add_view, name="task_add"),
    path('task/<int:pk>', detail_view, name='detail_view'),
    path("remove/<int:pk>", remove_view, name='remove_view')
]