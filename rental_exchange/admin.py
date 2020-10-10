from django.contrib import admin

# Register your models here.
from django.db import models
from django.forms import CheckboxSelectMultiple

from rental_exchange.forms import CarForm
from rental_exchange.models import Car, Brand, Feature, Tag


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Car._meta.fields]
    list_display_links = ['name']
    list_per_page = 10
    exclude = ('created_by', 'updated_by')
    autocomplete_fields = ['brand', 'tags']
    form = CarForm
    # formfield_overrides = {
    #     'features': {'widget': CheckboxSelectMultiple},
    # }


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Brand._meta.fields]
    list_display_links = ['name']
    list_per_page = 10
    search_fields = ['name']
    exclude = ('created_by', 'updated_by')


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Feature._meta.fields]
    list_display_links = ['title']
    list_per_page = 10
    exclude = ('created_by', 'updated_by')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tag._meta.fields]
    list_display_links = ['title']
    list_per_page = 10
    exclude = ('created_by', 'updated_by')
    search_fields = ['title']
