from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Sprint
from .models import Task
from .serializers import SprintSerializer
from .serializers import TaskSerializer
from .serializers import UserSerializer
from .mixin import DefaultsMixin


User = get_user_model()


class SprintViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = Sprint.objects.order_by('end')
    serializer_class = SprintSerializer


class TaskViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserViewSet(DefaultsMixin, viewsets.ReadOnlyModelViewSet):
    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.object.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer