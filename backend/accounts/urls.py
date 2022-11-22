from django.urls import path, include
from . import views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register("", views.AccountViewSet)

urlpatterns = [
    # path("signup/", views.SignupView.as_view(), name="signup"),
    
    path("register/",views.RegisterAPIView.as_view()),
    path("login/",views.LoginView.as_view()),
    # path("logout/",views.LogoutView.as_view()),
]