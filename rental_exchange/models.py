import datetime

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField


class Car(models.Model):
    TRANSMISSIONS = [
            ('Manual', 'Manual'),
            ('Automatic', 'Automatic')
    ]
    FUELS = [
        ('Gasoline', 'Gasoline'),
        ('Diesel', 'Diesel'),
        ('Liquefied Petroleum', 'Liquefied Petroleum'),
        ('Compressed Natural Gas', 'Compressed Natural Gas'),
        ('Ethanol', 'Ethanol'),
        ('Bio-diesel', 'Bio-diesel')
    ]
    PRICE_VARIATIONS = [
        ('Day', 'Day'),
        ('Month', 'Month'),
        ('Year', 'Year'),
    ]
    name = models.CharField(max_length=255, blank=False, null=False)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, blank=False, null=True)
    model_no = models.CharField(max_length=50, blank=False, null=False)
    model_year = models.IntegerField(validators=[MinValueValidator(1984), MaxValueValidator(datetime.date.today().year)], blank=False)
    mileage = models.IntegerField(default=0, blank=False, null=False)
    transmission = models.CharField(max_length=20, choices=TRANSMISSIONS, blank=False, null=False)
    seats = models.IntegerField(default=0, blank=False, null=False)
    luggage = models.IntegerField(default=0, blank=False, null=False)
    fuel = models.CharField(max_length=50, choices=FUELS, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    rental_price = MoneyField(max_digits=14, decimal_places=2, default=0.00, default_currency='USD', blank=False, null=False)
    price_variable = models.CharField(max_length=20, choices=PRICE_VARIATIONS, blank=False, null=False)
    features = models.ManyToManyField('Feature', blank=True)
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='rental_exchange/car_images', null=False, blank=False)
    tags = models.ManyToManyField('Tag', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="+")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "cars"
        verbose_name_plural = "Cars".upper()
        ordering = ("created_at",)
        unique_together = ('name', 'model_no', 'model_year')

    def get_absolute_url(self):
        return f"car/{self.id}/"


class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='rental_exchange/brand_images', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="+")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "brands"
        verbose_name_plural = "Brands".upper()
        ordering = ("name",)


class Feature(models.Model):
    title = models.CharField(max_length=255, unique=True, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="+")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "features"
        verbose_name_plural = "Features".upper()
        ordering = ("title",)


class Owner(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    country = CountryField(blank=False, null=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    image = models.ImageField(upload_to='rental_exchange/owner_images', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="+")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="+")

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = "owners"
        verbose_name_plural = "Owners".upper()
        ordering = ("id",)


class Customer(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    country = CountryField(blank=False, null=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    image = models.ImageField(upload_to='rental_exchange/customer_images', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="+")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="+")

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = "customers"
        verbose_name_plural = "Customers".upper()
        ordering = ("id",)


class Tag(models.Model):
    title = models.CharField(max_length=255, unique=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "tags"
        verbose_name_plural = "Tags".upper()
        ordering = ("title",)
