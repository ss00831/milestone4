from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Tourprogram(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    region = models.CharField(max_length=254)
    maximum = models.CharField(max_length=254)
    priceadult = models.IntegerField()
    pricechild = models.IntegerField()
    departure_date = models.CharField(max_length=254)
    estimated_times = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    included = models.CharField(max_length=254, null=True, blank=True)
    not_included = models.CharField(max_length=254, null=True, blank=True)
    meeting_place = models.CharField(max_length=254)
    note = models.TextField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name