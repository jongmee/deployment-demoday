from django.urls import path, include
from . import views
from menu.views import MenuViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", views.RestaurantViewSet)
router.register(r"(?P<restaurant_pk>\d+)/menu", MenuViewSet)

urlpatterns = [
    path("", include(router.urls)),
]