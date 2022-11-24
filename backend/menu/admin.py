from django.contrib import admin
from .models import Menu, Sale
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

@admin.register(Menu)
class MenuAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'menu_name', 'menu_price', 'restaurant')
    list_display_links = ('id', 'menu_name')
    pass


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    pass
