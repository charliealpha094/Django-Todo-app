# Generated by Django 3.0 on 2020-11-26 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_auto_20201125_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='Check',
            field=models.TextField(default='Yes/No'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateField(default='2020-11-26'),
        ),
    ]
