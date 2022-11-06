from django.db import models
from django.contrib.auth.models import User


class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    completed = models.BooleanField(default=False)
    date_completed = models.DateTimeField(null=True, blank=True)

    important = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = (
            'completed',
            'created',
        )

    def __str__(self):
        return f'{self.created}: {self.title}'
