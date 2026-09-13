from rest_framework import viewsets
from .models import Deal
from .serializers import DealSerializer

class DealViewSet(viewsets.ModelViewSet):
    queryset = Deal.objects.all().order_by('-created_at')
    serializer_class = DealSerializer
