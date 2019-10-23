from rest_framework import serializers

from .models import Task


class TaskSerializerers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'description', 'status')
