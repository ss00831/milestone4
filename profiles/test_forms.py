from django.test import TestCase
from .forms import UserProfileForm


# Create your tests here.
class TestUserProfileForms(TestCase):
    def test_create_profile_form_with_required_fields_filled(self):
        form = UserProfileForm({
            'full_name': 'tester',
            'email': 'testing@gmail.com',
            'phone_number': '+46721129441',
            'country': 'AU'})
        self.assertTrue(form.is_valid())
