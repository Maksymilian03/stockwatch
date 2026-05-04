from django.shortcuts import render

from rest_framework import viewsets
from .models import Stock
from .serializers import StockSerializer
from rest_framework import generics
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from .services import get_stock_price, get_stock_price_at_date
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status







# Create your views here.

class StockViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Stock.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    serializer_class = StockSerializer

    
    @action(detail=True, methods=['get'])
    def price(self, request, pk=None):
        ticker = Stock.objects.get(pk=pk, user=self.request.user)
        price = get_stock_price(ticker.symbol)
        if price is None:
             return Response({'error': 'Nie można pobrać ceny dla tego tickera'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'price': price, 'ticker': ticker.name})

    @action(detail=True, methods=['get'])
    def price_at_date(self, request, pk=None):
        ticker = Stock.objects.get(pk=pk, user=self.request.user)
        date = ticker.add_date.strftime('%Y-%m-%d')
        price = get_stock_price_at_date(ticker.symbol, date)

        if price is None:
            return Response({'error': 'Nie można pobrać ceny dla tego tickera'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'price': price, 'ticker': ticker.name})


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

