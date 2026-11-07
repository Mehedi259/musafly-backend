import logging
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import NotificationCampaign, DeviceToken, AppUser
from .serializers import NotificationCampaignSerializer, DeviceTokenSerializer, AppUserSerializer
from .firebase_service import send_push_notification

logger = logging.getLogger(__name__)

class NotificationCampaignViewSet(viewsets.ModelViewSet):
    queryset = NotificationCampaign.objects.all().order_by('-created_at')
    serializer_class = NotificationCampaignSerializer

    def perform_create(self, serializer):
        campaign = serializer.save()

        # Build absolute image URL if exists
        image_url = None
        if campaign.image:
            request = self.request
            try:
                image_url = request.build_absolute_uri(campaign.image.url)
            except Exception:
                image_url = campaign.image.url

        # Build payload for routing
        payload = {
            'notification_id': str(campaign.id),
            'target_type': campaign.target_type,
            'target_id': campaign.target_id or '',
            'external_link': campaign.external_link or '',
            'badge_text': campaign.badge_text or '',
        }

        # Send push notification via FCM
        fcm_result = send_push_notification(
            title=campaign.title,
            message=campaign.message,
            image_url=image_url,
            data_payload=payload
        )

        campaign.sent_count = fcm_result.get('success_count', 0)
        campaign.save(update_fields=['sent_count'])

    @action(detail=True, methods=['post'])
    def resend(self, request, pk=None):
        campaign = self.get_object()

        image_url = None
        if campaign.image:
            try:
                image_url = request.build_absolute_uri(campaign.image.url)
            except Exception:
                image_url = campaign.image.url

        payload = {
            'notification_id': str(campaign.id),
            'target_type': campaign.target_type,
            'target_id': campaign.target_id or '',
            'external_link': campaign.external_link or '',
            'badge_text': campaign.badge_text or '',
        }

        fcm_result = send_push_notification(
            title=campaign.title,
            message=campaign.message,
            image_url=image_url,
            data_payload=payload
        )

        campaign.sent_count += fcm_result.get('success_count', 0)
        campaign.save(update_fields=['sent_count'])

        return Response({
            'detail': 'Notification resent successfully.',
            'fcm_result': fcm_result
        }, status=status.HTTP_200_OK)


class RegisterDeviceTokenView(APIView):
    def post(self, request):
        token = request.data.get('token')
        if not token:
            return Response({'error': 'Token is required'}, status=status.HTTP_400_BAD_REQUEST)

        platform = request.data.get('platform', 'android')
        user_email = request.data.get('user_email', None)

        device, created = DeviceToken.objects.update_or_create(
            token=token,
            defaults={
                'platform': platform,
                'user_email': user_email,
                'is_active': True,
            }
        )

        serializer = DeviceTokenSerializer(device)
        return Response({
            'success': True,
            'created': created,
            'device': serializer.data
        }, status=status.HTTP_200_OK if not created else status.HTTP_201_CREATED)


class GoogleAuthView(APIView):
    def post(self, request):
        email = request.data.get('email')
        name = request.data.get('name')
        if not email or not name:
            return Response({'error': 'Email and name are required'}, status=status.HTTP_400_BAD_REQUEST)

        photo_url = request.data.get('photo_url', '')
        google_id = request.data.get('google_id', '')
        phone = request.data.get('phone', '')

        user, created = AppUser.objects.update_or_create(
            email=email,
            defaults={
                'name': name,
                'photo_url': photo_url,
                'google_id': google_id,
                'phone': phone if phone else None,
                'is_active': True,
            }
        )

        serializer = AppUserSerializer(user)
        return Response({
            'success': True,
            'is_new_user': created,
            'user': serializer.data
        }, status=status.HTTP_200_OK if not created else status.HTTP_201_CREATED)

