from django.urls import path, include
from . import views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register("", views.AccountViewSet)

urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="signup"),
]