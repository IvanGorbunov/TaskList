from django.forms import ModelForm

from todo.models import Tasks


class TaskForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ('user', 'title', 'description', 'date_completed', 'important')