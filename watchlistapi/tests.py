from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from watchlistapi.models import Stock
# Create your tests here.


class StockTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_create_stock(self):
        response = self.client.post('/stocks/', {'name': 'Test Stock', 'symbol': 'TST'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Stock.objects.count(), 1)

    def test_get_stocks(self):
        self.client.post('/stocks/', {'name': 'Test Stock', 'symbol': 'TST'})
        response = self.client.get('/stocks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/stocks/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_sees_only_own_stocks(self):
        self.client.post('/stocks/', {'name': 'Test Stock', 'symbol': 'TST'})
        self.client.post('/stocks/', {'name': 'Test Stock2', 'symbol': 'TST2'})

        self.client.force_authenticate(user=None)

        self.user2 = User.objects.create_user(username='testuser2', password='testpassword')
        self.client.force_authenticate(user=self.user2)

        self.client.post('/stocks/', {'name': 'Test Stock3', 'symbol': 'TST3'})

        response = self.client.get('/stocks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

        self.client.force_authenticate(user=None)
        self.client.force_authenticate(user=self.user)

        response = self.client.get('/stocks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)

    def test_delete_stock(self):
        response = self.client.post('/stocks/', {'name': 'Test Stock', 'symbol': 'TST'})
        stock_id = response.data['id']
        response = self.client.delete(f'/stocks/{stock_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Stock.objects.count(), 0)





