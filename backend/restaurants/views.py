from django.shortcuts import render
from .models import Restaurant, TypeCategory, LocationCategory
from .serializers import RestaurantSerializer, TypeCategorySerializer, LocationCategorySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

class RestaurantViewSet(ModelViewSet):
     queryset = Restaurant.objects.all()
     serializer_class = RestaurantSerializer

class TypeCategoryViewSet(ListAPIView):
     queryset = TypeCategory.objects.all()
     serializer_class = TypeCategorySerializer

class LocationCategoryViewSet(ListAPIView):
     queryset =LocationCategory.objects.all()
     serializer_class = LocationCategorySerializer