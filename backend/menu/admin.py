from django.contrib import admin
from .models import Menu, Sale


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    pass
