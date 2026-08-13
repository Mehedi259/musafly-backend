from rest_framework import viewsets
from .models import UmrahPackage
from .serializers import UmrahPackageSerializer

class UmrahPackageViewSet(viewsets.ModelViewSet):
    queryset = UmrahPackage.objects.all()
    serializer_class = UmrahPackageSerializer
