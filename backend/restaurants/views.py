from django.shortcuts import render
from .models import Restaurant
from .serializers import RestaurantSerializer
from rest_framework.viewsets import ModelViewSet

class RestaurantViewSet(ModelViewSet):
     queryset = Restaurant.objects.all()
     serializer_class = RestaurantSerializer
