from django.contrib import admin
from .models import Restaurant, TypeCategory, LocationCategory
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

@admin.register(TypeCategory)
class TypeCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(LocationCategory)
class LocationCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Restaurant)
class RestaurantAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'store_name', 'type', 'location_type')
    list_display_links = ('id', 'store_name')
    pass
