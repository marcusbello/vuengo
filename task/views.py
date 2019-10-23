from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializerers

# Create your views here.

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class TaskViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows task to be viewed or edited
    """

    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializerers