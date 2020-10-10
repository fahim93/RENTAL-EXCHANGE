from django.shortcuts import render

# Create your views here.
from django.views import generic

from rental_exchange.models import Car


def home_view(request):
    cars = Car.objects.filter(is_featured=True)
    context = {
        "title": "Rental Exchange",
        "cars": cars
    }
    return render(request, 'rental_exchange/containers/home.html', context)


def about_view(request):
    context = {
        "title": "About - Rental Exchange"
    }
    return render(request, 'rental_exchange/containers/about.html', context)


def blog_view(request):
    context = {
        "title": "Blog - Rental Exchange"
    }
    return render(request, 'rental_exchange/containers/blog.html', context)


def blog_detail_view(request):
    context = {
        "title": "Blog Details - Rental Exchange"
    }
    return render(request, 'rental_exchange/containers/blog-single.html', context)


def contact_view(request):
    context = {
        "title": "Contact - Rental Exchange"
    }
    return render(request, 'rental_exchange/containers/contact.html', context)


def pricing_view(request):
    context = {
        "title": "Pricing - Rental Exchange"
    }
    return render(request, 'rental_exchange/containers/pricing.html', context)


def car_view(request):
    context = {
        "title": "Car - Rental Exchange"
    }
    return render(request, 'rental_exchange/containers/car.html', context)


def car_detail_view(request):
    context = {
        "title": "Car Detail - Rental Exchange"
    }
    return render(request, 'rental_exchange/containers/car-single.html', context)


def admin_home_view(request):
    context = {
        "title": "Admin Dashboard - Rental Exchange"
    }
    return render(request, 'rental_exchange/admin/containers/home.html', context)


def admin_blank_view(request):
    context = {
        "title": "Blank - Rental Exchange"
    }
    return render(request, 'rental_exchange/admin/containers/blank.html', context)


class CarDetailView(generic.DetailView):
    model = Car
    template_name = 'rental_exchange/containers/car-single.html'
