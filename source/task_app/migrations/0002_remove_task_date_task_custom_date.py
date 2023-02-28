# Generated by Django 4.1.6 on 2023-02-17 05:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='date',
        ),
        migrations.AddField(
            model_name='task',
            name='custom_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 17, 5, 11, 10, 106750, tzinfo=datetime.timezone.utc), verbose_name='custom_date'),
        ),
    ]