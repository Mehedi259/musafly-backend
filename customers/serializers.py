from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    joined_date = serializers.DateField(format="%b %d, %Y", input_formats=['%Y-%m-%d', 'iso-8601'])
    class Meta:
        model = Customer
        fields = '__all__'
