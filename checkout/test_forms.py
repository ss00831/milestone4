from django.test import TestCase
from .forms import OrderForm


# Create your tests here.
class TestOrderForm(TestCase):

    def test_create_order(self):
        form = OrderForm({
            'full_name': 'peter',
            'email': 'peter.xxsson@gmail.com',
            'phone_number': '0702214431',
            'country': 'CA'})
        self.assertTrue(form.is_valid())

    def test_correct_message(self):
        form = OrderForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['full_name'], [u'This field is required.'])
