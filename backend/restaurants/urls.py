from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.RestaurantListAPIView.as_view(), name='restaurant_list'),
]