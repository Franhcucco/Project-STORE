from django.contrib import admin
from django.urls import path, include

from products.views import *
urlpatterns = [
    path ('shoes_list/', shoes_list),
    path ('tshirts_list/', tshirts_list),
    path ('pants_list/', pants_list),
    path ('create_pants/', create_pants),
    path ('create_tshirts/', create_tshirts),
    path ('create_shoes/', create_shoes),
    path ('products_list/', products_list)
]