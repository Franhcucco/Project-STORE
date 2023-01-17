from django.contrib import admin
from subscriptions.models import *
# Register your models here.

@admin.register(subscriptions)
class SubscriptionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail')