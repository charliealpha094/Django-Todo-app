# Generated by Django 3.0 on 2020-11-24 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_todo_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='due_date',
            field=models.TextField(default='Insert expire date'),
        ),
    ]
