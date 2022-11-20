from django.urls import path, include
from . import views
from menu.views import MenuListAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", views.RestaurantViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("<int:restaurant_pk>/menu/", MenuListAPIView.as_view(), name='menu_list'),
]