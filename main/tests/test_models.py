from decimal import Decimal
from django.test import TestCase
from main.models import Product


class TestModel(TestCase):
    def test_active_manager_works(self):
        Product.objects.create(
            name="Learning Python 3.8",
            price=Decimal("20.00")
        )
        Product.objects.create(
            name="Learning Python 3.7",
            price=Decimal("10.00")
        )
        Product.objects.create(
            name="Learning Python 3.6",
            price=Decimal("5.00"),
            active=False
        )
        self.assertEqual(len(Product.objects.active()), 2)
        self.assertEqual(len(Product.objects.all()), 3)
