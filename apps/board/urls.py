from rest_framework.routers import DefaultRouter
from .views import SprintViewSet
from .views import TaskViewSet
from .views import UserViewSet


router = DefaultRouter()

router.register(r'sprint', SprintViewSet)
router.register(r'task', TaskViewSet)
router.register(r'user', UserViewSet)