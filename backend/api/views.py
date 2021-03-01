from django.conf import settings
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from tasks.models import Task
from api import serializers
from api.permissions import IsTaskOwner


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = [IsAuthenticated, IsTaskOwner]


class TaskList(generics.ListCreateAPIView):
    serializer_class = serializers.TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
