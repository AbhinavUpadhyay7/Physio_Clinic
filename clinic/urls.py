from django.urls import path
from .views import home

from .views import (
    home,
    doctor,
    contact,
    gallery
)

urlpatterns = [
    path('', home, name='home'),
    path('doctor/', doctor, name='doctor'),
    path('contact/', contact, name='contact'),
    path('gallery/', gallery, name='gallery')
]