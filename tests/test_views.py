from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setup():
        Menu.objects.create(title="Ice Cream", price=7.50, inventory=100)
        Menu.objects.create(title="Grilled Fish", price=12.50, inventory=20)
        Menu.objects.create(title="Greek Salad", price=6.25, inventory=75)
        Menu.objects.create(title="Salmon en Croute", price=15.00, inventory=50)
        Menu.objects.create(title="Chocolate Cake", price=6.99, inventory=80)
        
    def test_get_all(self):
        items = Menu.objects.all()
        serialized_items = MenuSerializer(items, many=True)
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.data, serialized_items.data)