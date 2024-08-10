from django.urls import path
from .views import create_product,home

urlpatterns = [
    path('',home,name='home'),
    path('form/', create_product, name='form'),
   
]
