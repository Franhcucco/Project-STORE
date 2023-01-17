from django.contrib import admin
from products.models import *

@admin.register(shoes)
class ShoesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'size', 'stock')

@admin.register(tShirt)
class TShirtsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'size', 'stock')

@admin.register(pants)
class PantsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'size', 'stock')