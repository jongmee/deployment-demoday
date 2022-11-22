from rest_framework import serializers
from .models import Restaurant, TypeCategory, LocationCategory

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class TypeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeCategory
        fields = '__all__'

class LocationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationCategory
        fields = '__all__'