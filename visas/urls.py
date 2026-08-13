from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VisaViewSet

router = DefaultRouter()
router.register(r'visas', VisaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
