from django.urls import path
from rental_exchange import views
urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('blog/', views.blog_view, name='blog'),
    path('blog-detail', views.blog_detail_view, name='blog-detail'),
    path('pricing', views.pricing_view, name='pricing'),
    path('contact', views.contact_view, name='contact'),
    path('car', views.car_view, name='car'),
    # path('car/<id>/', views.car_detail_view, name='car-detail'),
    # path('car-detail', views.car_detail_view, name='car-detail'),
    path('car/<int:pk>/', views.CarDetailView.as_view(), name='car-detail'),

    # admin
    path('re-admin/', views.admin_home_view, name='admin-home'),
    path('re-admin/blank/', views.admin_blank_view, name='admin-blank'),
]