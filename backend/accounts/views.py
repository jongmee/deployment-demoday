from .serializers import SignupSerializer
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model


class SignupView(CreateAPIView):
    model = get_user_model()
    serializer_class = SignupSerializer