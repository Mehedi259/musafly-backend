from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotificationCampaignViewSet, RegisterDeviceTokenView, GoogleAuthView

router = DefaultRouter()
router.register(r'notifications', NotificationCampaignViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('devices/register/', RegisterDeviceTokenView.as_view(), name='register-device'),
    path('auth/google/', GoogleAuthView.as_view(), name='auth-google'),
]

