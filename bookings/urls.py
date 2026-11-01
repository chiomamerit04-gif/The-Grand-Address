from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('properties/', views.property_list, name='property_list'),
    path('property-details/<int:property_id>/', views.property_detail, name='property_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('book/<int:property_id>/', views.booking_view, name='booking'),
    path('booking-success/<int:booking_id>/', views.booking_success, name='booking_success'),
]