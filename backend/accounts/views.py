from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from restaurants.models import Restaurant
from menu.models import Menu
from rest_framework.generics import get_object_or_404

User=get_user_model()

# class SignupView(CreateAPIView):
#     model = get_user_model()
#     serializer_class = SignupSerializer

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "register successs",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            res.set_cookie("access", access_token, httponly=True)
            res.set_cookie("refresh", refresh_token, httponly=True)
            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request): #디버깅용
        re = User.objects.all()
        re2 = RegisterSerializer(re, many=True)
        return Response(re2.data)

class LoginView(APIView):
    def post(self, request):
        user = authenticate(
            User_name=request.data.get("nickname"), password=request.data.get("password")
        )
        if user is not None:
            serializer = UserSerializer(user)
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "login success",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            return res
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def get(self, request): #디버깅용
        re = User.objects.all()
        re2 = UserSerializer(re, many=True)
        return Response(re2.data)

@api_view(["POST"])
def add_mymenu(request):
    menu_name = request.data["menu_name"]
    menu = get_object_or_404(Menu, menu_name=menu_name)
    request.user.my_menu.add(menu)
    return Response(status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def add_mystore(request):
    store_name = request.data["store_name"]
    store = get_object_or_404(Restaurant, store_name=store_name)
    request.user.my_store.add(store)
    return Response(status.HTTP_204_NO_CONTENT)