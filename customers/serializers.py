from rest_framework import serializers
from .models import Customer
from datetime import datetime

class CustomerSerializer(serializers.ModelSerializer):
    joined_date = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = '__all__'
        
    def get_joined_date(self, obj):
        if not obj.joined_date:
            return None
        # Handle both date and datetime objects
        d = obj.joined_date.date() if isinstance(obj.joined_date, datetime) else obj.joined_date
        return d.strftime("%b %d, %Y")
