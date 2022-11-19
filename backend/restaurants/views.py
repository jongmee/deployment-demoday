from django.shortcuts import render
from .models import Restaurant
from .serializers import RestaurantSerializer
from rest_framework.generics import ListAPIView

class RestaurantListAPIView(ListAPIView):
     queryset = Restaurant.objects.all()
     serializer_class = RestaurantSerializer
