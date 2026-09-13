from rest_framework import viewsets
from .models import Transaction, MonthlyStat
from .serializers import TransactionSerializer, MonthlyStatSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by('-id')
    serializer_class = TransactionSerializer

class MonthlyStatViewSet(viewsets.ModelViewSet):
    queryset = MonthlyStat.objects.all().order_by('id')
    serializer_class = MonthlyStatSerializer
