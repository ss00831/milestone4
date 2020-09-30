from django.test import TestCase
from checkout.models import Order


# Create your tests here.
class TestCheckoutModels(TestCase):

    fixtures = [
        'categories.json',
        'tourprograms.json',
    ]

    @classmethod
    def setUpTestData(cls):
        Order.objects.create(
            order_number=000,
            full_name="tester",
            email='tester@gmail.com',
            phone_number='0723312496',
            country='SE',
        )

    def test_Checkout_details(self):
        order = Order.objects.get(id=1)
        self.assertEqual(order.full_name, 'tester')
        self.assertEqual(order.email, 'tester@gmail.com')

    def test_Checkout_generate_order_number(self):
        order = Order.objects.get(id=1)
        self.assertFalse(order.order_number == 000)
