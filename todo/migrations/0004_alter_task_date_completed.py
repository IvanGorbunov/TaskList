# Generated by Django 3.2.7 on 2021-09-21 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_rename_tasks_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
