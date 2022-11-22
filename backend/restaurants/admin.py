from django.contrib import admin
from .models import Restaurant, TypeCategory, LocationCategory

@admin.register(TypeCategory)
class TypeCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(LocationCategory)
class LocationCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    pass
