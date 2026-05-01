from django.shortcuts import render

from rest_framework import viewsets
from .models import Stock
from .serializers import StockSerializer
from rest_framework import generics
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny



# Create your views here.

class StockViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Stock.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    serializer_class = StockSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]