from django.contrib import admin
from .models import Tasks


class TaskAdmin(admin.ModelAdmin):
    verbose_name_plural = 'Задачи'
    readonly_fields = ('created',)


admin.site.register(Tasks, TaskAdmin)
