from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="MusaFly API",
        default_version='v1',
        description="API documentation for MusaFly backend",
        terms_of_service="https://www.musafly.com/terms/",
        contact=openapi.Contact(email="contact@musafly.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # App URLs
    path('api/', include('tours.urls')),
    path('api/', include('flights.urls')),
    path('api/', include('visas.urls')),
    path('api/', include('umrah.urls')),
    path('api/', include('testimonials.urls')),
    path('api/', include('faqs.urls')),
    path('api/', include('inventory.urls')),
    path('api/', include('customers.urls')),
    path('api/', include('reports.urls')),
    path('api/', include('marketing.urls')),
    
    # Swagger URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # In production, usually web server handles this, but for simplicity with gunicorn:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
