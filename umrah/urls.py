from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UmrahPackageViewSet

router = DefaultRouter()
router.register(r'umrah', UmrahPackageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
