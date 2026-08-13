from rest_framework import serializers
from .models import UmrahPackage

class UmrahPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UmrahPackage
        fields = '__all__'
