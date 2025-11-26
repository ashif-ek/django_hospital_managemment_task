from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('booking/', views.booking, name='booking'),
    path('booking/confirmation/', views.booking_confirmation, name='booking_confirmation'),
    path('doctors/', views.doctors, name='doctors'),
    path('department/', views.department, name='department'),
    path('contact/', views.contact, name='contact'),
    
]
