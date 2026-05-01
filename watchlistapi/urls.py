from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlistapi.views import StockViewSet, RegisterView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('stocks', StockViewSet, basename='stock')




urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login')
]
