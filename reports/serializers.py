from rest_framework import serializers
from .models import Transaction, MonthlyStat

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class MonthlyStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyStat
        fields = '__all__'
