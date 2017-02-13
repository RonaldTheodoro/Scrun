from rest_framework.routers import DefaultRouter
from .views import SprintViewSet
from .views import TaskViewSet
from .views import UserViewSet


router = DefaultRouter(trailing_slash=False)

router.register(r'sprints', SprintViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'users', UserViewSet)
