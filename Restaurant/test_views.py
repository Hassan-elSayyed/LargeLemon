from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import MenuItem
from .serializers import MenuItemSerializer

# PATH = '/restaurant/menu-items/'

# class MenuViewTest(TestCase):
#     def setUp(self):  # note: it's setUp(), not `setup`
#         self.client = APIClient()
#         MenuItem.objects.create(title="IceCream", price="80.00", inventory=100)
#         MenuItem.objects.create(title="Pizza",     price="50.50", inventory=200)
#         MenuItem.objects.create(title="Pasta",     price="42.00", inventory=150)

#     def test_getall(self):
#         url = reverse("restaurant/menu-items/")
#         resp = self.client.get(url)

#         self.assertEqual(resp.status_code, 200)

#         items = MenuItem.objects.all().order_by("id")
#         expected = MenuItemSerializer(items, many=True).data

#         # DRF’s APIClient gives you resp.data (already parsed).
#         self.assertEqual(resp.data, expected)

# from django.test import TestCase
# from rest_framework.test import APIClient

# from .models import MenuItem
# from .serializers import MenuItemSerializer

# MENU_ITEMS_URL = 'restaurant/menu-items/'

# class MenuItemViewTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         MenuItem.objects.create(title='IceCream', price=80, inventory=100)
#         MenuItem.objects.create(title='Pizza', price=50.50, inventory=200)
#         MenuItem.objects.create(title='Pasta', price=42, inventory=150)
    
#     def test_getall(self):
#         resp = self.client.get(MENU_ITEMS_URL)
#         self.assertEqual(resp.status_code, 200)
        
#         items = MenuItem.objects.all().order_by('id)')
#         expected = MenuItemSerializer(items, many=True).data
        
#         self.assertEqual(resp.data, expected)
                        
                        
from django.test import TestCase, override_settings
from rest_framework.test import APIClient
from django.urls import resolve
from decimal import Decimal

from .models import MenuItem
from .serializers import MenuItemSerializer

PATH = "/restaurant/menu-items/"

# If resolve(PATH) fails, uncomment the decorator and set your project urls:
# @override_settings(ROOT_URLCONF="LittleLemon.urls")
class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        MenuItem.objects.create(title="IceCream", price=Decimal("80.00"), inventory=100)
        MenuItem.objects.create(title="Pizza",    price=Decimal("50.50"), inventory=200)
        MenuItem.objects.create(title="Pasta",    price=Decimal("42.00"), inventory=150)

    def test_getall(self):
        # Sanity: does the URL resolve to the expected view?
        match = resolve(PATH)
        assert match.func.view_class.__name__ == "MenuItemsView"

        # GET (follow redirects just in case APPEND_SLASH meddles)
        resp = self.client.get(PATH, follow=True)
        self.assertEqual(resp.status_code, 200, f"redirect_chain={resp.redirect_chain}")

        expected = MenuItemSerializer(MenuItem.objects.all().order_by("id"), many=True).data
        self.assertEqual(resp.data, expected)
                        