from django.urls import path, include
from . import views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register("", views.AccountViewSet)

urlpatterns = [
    path("register/",views.RegisterAPIView.as_view()),
    path("login/",views.LoginView.as_view()),
    path("mystore/", views.add_mystore),
    path("mymenu/", views.add_mymenu),
    path("show-mystore/", views.show_mystore),
    path("show-mymenu/", views.show_mymenu),
]