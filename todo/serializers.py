from rest_framework import serializers
from todo.models import Tasks


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id', 'user', 'title', 'description', 'created', 'date_completed', 'important')

    def create(self, validated_data):
        """
        Создать и вернуть новый "Tasks" объект по полученным проверенным данным
        """
        return Tasks.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Обновить и вернуть существующий `Tasks` объект по полученным проверенным данным.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.user = validated_data.get('user', instance.user)
        instance.description = validated_data.get('description', instance.description)
        instance.created = validated_data.get('created', instance.created)
        instance.date_completed = validated_data.get('date_completed', instance.date_completed)
        instance.important = validated_data.get('important', instance.important)
        instance.save()
        return instance
