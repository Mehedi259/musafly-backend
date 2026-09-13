from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet, MonthlyStatViewSet

router = DefaultRouter()
router.register(r'reports/transactions', TransactionViewSet)
router.register(r'reports/monthly', MonthlyStatViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
