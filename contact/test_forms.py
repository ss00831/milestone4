from django.test import TestCase
from .forms import ContactForm


# Create your tests here.
class TestContactForm(TestCase):
    def test_send_message(self):
        form = ContactForm({
            'contact_type': 5,
            'name': 'Mina',
            'tour_program_name': 'Wildness Meal',
            'order_number': 'se00dfwdsmqjk',
            'phone': '+821032214431',
            'email': 'Mina.lee@gmail.com',
            'message': 'Can you speak Korean?'})
        self.assertTrue(form.is_valid())

    def test_correct_message(self):
        form = ContactForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])
