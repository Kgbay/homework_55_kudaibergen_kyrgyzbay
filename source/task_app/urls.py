from django.urls import path

from .views.base import index_view
from .views.tasks import add_view, detail_view, remove_view, update_view, confirm_delete_view

urlpatterns = [
    path("", index_view, name='index'),
    path("task/add/", add_view, name="task_add"),
    path('task/<int:pk>', detail_view, name='detail_view'),
    path("remove/<int:pk>", remove_view, name='remove_view'),
    path("task/<int:pk>/confirm_delete", confirm_delete_view, name='confirm_delete'),
    path("task/<int:pk>/update/", update_view, name='task_update')
]