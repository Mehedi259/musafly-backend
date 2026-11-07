from rest_framework import serializers
from .models import NotificationCampaign, DeviceToken, AppUser

class NotificationCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationCampaign
        fields = '__all__'


class DeviceTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceToken
        fields = ['id', 'token', 'platform', 'user_email', 'is_active', 'created_at']
        extra_kwargs = {
            'token': {'validators': []}  # Handled via update_or_create
        }


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['id', 'email', 'name', 'photo_url', 'google_id', 'phone', 'created_at', 'last_login']

