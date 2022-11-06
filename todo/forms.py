from django.forms import ModelForm, TextInput

from todo.models import Tasks


class TaskForm(ModelForm):
    class Meta:
        model = Tasks
        fields = (
            'user',
            'title',
            # 'description',
            # 'date_completed',
            # 'important',
        )

        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            # 'description': TextInput(attrs={'class': 'form-control'}),
        }
