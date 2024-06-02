from rest_framework import routers
from .viewsets import UserViewSet

app_name = 'account'

router = routers.SimpleRouter()

router.register("users", UserViewSet, basename="api-users")