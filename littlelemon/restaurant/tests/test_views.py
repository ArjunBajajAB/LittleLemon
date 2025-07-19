from django.test import TestCase
from restaurant.views import MenuItemView
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setup(self):
        item = Menu.objects.create(title="IceCream", price = 80, inventory = 100)
    
    def test_getall(self):
        menu_items = Menu.objects.all()

