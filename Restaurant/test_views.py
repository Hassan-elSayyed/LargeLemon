from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import MenuItem
from .serializers import MenuItemSerializer
                        
                        
from django.test import TestCase, override_settings
from rest_framework.test import APIClient
from django.urls import resolve
from decimal import Decimal

from .models import MenuItem
from .serializers import MenuItemSerializer

PATH = "/restaurant/api/menu-items/"

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        MenuItem.objects.create(title="IceCream", price=Decimal("80.00"), inventory=100)
        MenuItem.objects.create(title="Pizza",    price=Decimal("50.50"), inventory=200)
        MenuItem.objects.create(title="Pasta",    price=Decimal("42.00"), inventory=150)

    def test_getall(self):
        resp = self.client.get(PATH, follow=True)
        self.assertEqual(resp.status_code, 200, f"redirect_chain={resp.redirect_chain}")

        expected = MenuItemSerializer(MenuItem.objects.all().order_by("id"), many=True).data
        self.assertEqual(resp.data, expected)
                        