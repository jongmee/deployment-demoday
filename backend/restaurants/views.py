from django.shortcuts import render
from .models import Restaurant, TypeCategory, LocationCategory
from .serializers import RestaurantSerializer, TypeCategorySerializer, LocationCategorySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


class RestaurantViewSet(ModelViewSet):
     queryset = Restaurant.objects.all()
     serializer_class = RestaurantSerializer

class TypeCategoryViewSet(ListAPIView):
     queryset = TypeCategory.objects.all()
     serializer_class = TypeCategorySerializer

class LocationCategoryViewSet(ListAPIView):
     queryset = LocationCategory.objects.all()
     serializer_class = LocationCategorySerializer


@api_view(["GET"])
def show_mystore(request):
     user = request.user
     my_stores = user.my_store.all()
     serializer = RestaurantSerializer(my_stores, many=True)
     return Response(serializer.data)