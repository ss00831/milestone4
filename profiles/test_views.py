from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


# Create your tests here.
# https://docs.djangoproject.com/en/3.1/topics/testing/tools/
class TestProfileViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="Mimi", email="mimi@test.com", password="xmdnltmxmzld1!")

    def test_user_Profile_view(self):
        user = self.client.login(
            email="mimi@test.com", password="xmdnltmxmzld1!")
        resp = self.client.get(reverse('profile'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name="profiles/profile.html")


class TestProfileDetailViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="Mimi", email="mimi@test.com", password="xmdnltmxmzld1!")

    def test_profile(self):
        user = self.client.login(
            email="mimi@test.com", password="xmdnltmxmzld1!")
        resp = self.client.get(reverse('profile'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(
            resp, template_name="profiles/profile.html")
