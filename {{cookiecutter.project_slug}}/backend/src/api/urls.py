from django.urls import path, include
from rest_framework import routers

from account.urls import router as account_router

router = routers.DefaultRouter()

router.registry.extend(account_router.registry)

urlpatterns = [
    path('', include(router.urls)),
]