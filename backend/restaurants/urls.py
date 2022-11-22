from django.urls import path, include
from . import views
from menu.views import MenuViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("all", views.RestaurantViewSet)
router.register(r"(?P<restaurant_pk>\d+)/menu", MenuViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("type/", views.TypeCategoryViewSet.as_view()),
    path("locationtype/", views.LocationCategoryViewSet.as_view()),
    path("mystore/", views.show_mystore),
]