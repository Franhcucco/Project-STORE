from django.contrib import admin
from django.urls import path, include

from subscriptions.views import *

urlpatterns = [
    path('create_subscription/', subscription),
]