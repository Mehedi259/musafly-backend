import logging
import os
from django.conf import settings

logger = logging.getLogger(__name__)

try:
    import firebase_admin
    from firebase_admin import credentials, messaging
    FIREBASE_INSTALLED = True
except ImportError:
    FIREBASE_INSTALLED = False

_firebase_app = None

def get_firebase_app():
    global _firebase_app
    if not FIREBASE_INSTALLED:
        logger.warning("firebase-admin package is not installed.")
        return None

    if _firebase_app is not None:
        return _firebase_app

    try:
        # Check if already initialized by default
        _firebase_app = firebase_admin.get_app()
        return _firebase_app
    except ValueError:
        pass

    # Look for firebase credentials file
    cred_paths = [
        os.path.join(settings.BASE_DIR, 'firebase_credentials.json'),
        os.path.join(settings.BASE_DIR, 'config', 'firebase_credentials.json'),
        os.path.join(settings.BASE_DIR, 'notifications', 'firebase_credentials.json'),
    ]

    cred_file = None
    for p in cred_paths:
        if os.path.exists(p):
            cred_file = p
            break

    if cred_file:
        try:
            cred = credentials.Certificate(cred_file)
            _firebase_app = firebase_admin.initialize_app(cred)
            logger.info("Firebase Admin successfully initialized from %s", cred_file)
            return _firebase_app
        except Exception as e:
            logger.error("Failed to initialize Firebase with %s: %s", cred_file, e)
            return None
    else:
        logger.info("No firebase_credentials.json found. Push notifications will be queued or logged.")
        return None


def send_push_notification(title, message, image_url=None, data_payload=None, tokens=None):
    """
    Sends FCM Push Notification to list of tokens or all active DeviceTokens.
    Returns: dict(success_count=int, failure_count=int, message=str)
    """
    app = get_firebase_app()
    if not app:
        return {
            'success_count': 0,
            'failure_count': 0,
            'message': 'Firebase Admin not configured or credentials not loaded. Stored in DB successfully.'
        }

    from .models import DeviceToken

    if tokens is None:
        tokens = list(DeviceToken.objects.filter(is_active=True).values_list('token', flat=True))

    if not tokens:
        return {
            'success_count': 0,
            'failure_count': 0,
            'message': 'No registered active devices found.'
        }

    notification_payload = messaging.Notification(
        title=title,
        body=message,
        image=image_url if image_url else None
    )

    clean_data = {}
    if data_payload:
        for k, v in data_payload.items():
            clean_data[str(k)] = str(v) if v is not None else ''

    success_count = 0
    failure_count = 0

    # FCM allows batches of up to 500 tokens in send_each_for_multicast
    batch_size = 500
    for i in range(0, len(tokens), batch_size):
        batch = tokens[i:i + batch_size]
        multicast_msg = messaging.MulticastMessage(
            tokens=batch,
            notification=notification_payload,
            data=clean_data,
            android=messaging.AndroidConfig(
                priority='high',
                notification=messaging.AndroidNotification(
                    icon='ic_notification',
                    color='#1E3A8A',
                    image=image_url if image_url else None,
                    sound='default',
                )
            ),
            apns=messaging.APNSConfig(
                payload=messaging.APNSPayload(
                    aps=messaging.Aps(
                        sound='default',
                        badge=1
                    )
                )
            )
        )

        try:
            response = messaging.send_each_for_multicast(multicast_msg)
            success_count += response.success_count
            failure_count += response.failure_count

            # Cleanup expired or invalid tokens
            if response.failure_count > 0:
                for idx, resp in enumerate(response.responses):
                    if not resp.success:
                        bad_token = batch[idx]
                        err_code = resp.exception.code if hasattr(resp.exception, 'code') else ''
                        if err_code in ['registration-token-not-registered', 'invalid-argument']:
                            DeviceToken.objects.filter(token=bad_token).delete()

        except Exception as e:
            logger.error("Error sending FCM multicast batch: %s", e)
            failure_count += len(batch)

    return {
        'success_count': success_count,
        'failure_count': failure_count,
        'message': f'FCM delivered: {success_count} success, {failure_count} failed.'
    }

