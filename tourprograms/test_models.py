from django.test import TestCase
from tourprograms.models import Tourprogram


# Create your tests here.
class TourprogramModelTests(TestCase):

    # https://docs.djangoproject.com/en/3.1/topics/testing/tools/
    @classmethod
    def setUpTestData(cls):
        Tourprogram.objects.create(
            sku='LSPROGRAM0019',
            name="Summer tour test",
            region='Kiruna',
            maximum=999,
            priceadult=1500,
            pricechild=1100,
            departure_date='April – September. Daily. 11.30-14.30',
            estimated_times='3 hours',
            description="Test",
            rating=3.45,
            included='Coffee',
            not_included='Transfer',
            meeting_place='Kiruna Bus terminal',
            note='none',
            image_url='',
            image='',
        )

    def test_tourprogram_name(self):
        tourprogram = Tourprogram.objects.get(id=1)
        self.assertEqual(tourprogram.name, "Summer tour test")

    def test_tourprograms_description(self):
        tourprogram = Tourprogram.objects.get(id=1)
        self.assertEqual(tourprogram.description, "Test")

    def test_tourprograms_image(self):
        tourprogram = Tourprogram.objects.get(id=1)
        self.assertEqual(tourprogram.image, '')
