from django.test import TestCase
from .forms import UserProfileForm


# Create your tests here.
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing
class TestUserProfileForms(TestCase):
    def test_create_profile_form_filled(self):
        form = UserProfileForm({
            'full_name': 'tester',
            'email': 'testing@gmail.com',
            'phone_number': '+46721129441',
            'country': 'AU'})
        self.assertTrue(form.is_valid())
