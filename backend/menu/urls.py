from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'all', views.AllMenuViewSet, 'all')
router.register(r'sale', views.SaleMenuViewSet, 'sale')

urlpatterns = [
    path("", include(router.urls)),
    path("allsale/", views.SaleListAPIView.as_view()),
    path("mymenu/", views.show_mymenu),
]