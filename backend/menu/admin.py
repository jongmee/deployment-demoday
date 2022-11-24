from django.contrib import admin
from .models import Menu, Sale
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

@admin.register(Menu)
class MenuAdmin(ImportExportMixin, admin.ModelAdmin):
    pass


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    pass
