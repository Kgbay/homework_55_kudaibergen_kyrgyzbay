from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


class StatusChoice(TextChoices):
    ACTIVE = ('ACTIVE', 'Активна')
    NOT_ACTIVE = ('NOT_ACTIVE', 'Неактивна')

# Create your models here.
class Task(models.Model):
    title = models.TextField(max_length=200, null=False, verbose_name="Заголовок", default='Заголовок не задан')
    full_desc = models.TextField(max_length=3000, null=True, verbose_name='Полное описание')
    status = models.CharField(max_length=20, verbose_name="Статус", choices=StatusChoice.choices, default=StatusChoice.ACTIVE)
    author = models.CharField(max_length=200, null=False, blank=False, verbose_name="Автор")
    custom_date = models.DateField(verbose_name="custom_date", null=False, default=timezone.now())
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")
    is_deleted = models.BooleanField(verbose_name='удалено', null=False, default=False)
    deleted_at = models.DateTimeField(verbose_name='Дата и время удаления', null=True, default=None)



    def __str__(self):
        return f"{self.author} - {self.title}"
