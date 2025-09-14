from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name= 'contact'),
    path('menu/', menu, name='menu'),
    path('feedback/', feedback_view, name='feedback'),
]