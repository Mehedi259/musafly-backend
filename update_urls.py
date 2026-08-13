import os

filepath = '/Users/mehedihasanmridul/website/musafly-backend/config/urls.py'
with open(filepath, 'r') as f:
    content = f.read()

# Add imports for media serving
if 'from django.conf import settings' not in content:
    content = content.replace(
        'from django.urls import path, include',
        'from django.urls import path, include\nfrom django.conf import settings\nfrom django.conf.urls.static import static'
    )

# Append static media serve
if '+ static(settings.MEDIA_URL' not in content:
    content = content + '\n\nif settings.DEBUG:\n    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\nelse:\n    # In production, usually web server handles this, but for simplicity with gunicorn:\n    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\n'

with open(filepath, 'w') as f:
    f.write(content)

