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
from menu.serializers import MenuSerializer
from restaurants.serializers import RestaurantSerializer
import jwt

User = get_user_model()

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

    def get(self, request):  # 디버깅용
        re = User.objects.all()
        re2 = RegisterSerializer(re, many=True)
        return Response(re2.data)


class LoginView(APIView):
    def post(self, request):
        user = authenticate(
            username=request.data.get("username"), password=request.data.get("password")
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
            return Response(
                {
                    "user": request.data.get('username'),
                    "message": "login failed",
                }, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):  # 디버깅용
        re = User.objects.all()
        re2 = UserSerializer(re, many=True)
        return Response(re2.data)
    # 로그아웃

    def delete(self, request):
        # 쿠키에 저장된 토큰 삭제 => 로그아웃 처리
        response = Response({
            "message": "Logout success"
        }, status=status.HTTP_202_ACCEPTED)
        response.delete_cookie("access")
        response.delete_cookie("refresh")
        return response



@api_view(["POST"])
def add_mymenu(request):
    menu_name = request.data["menu_name"]
    menu = get_object_or_404(Menu, menu_name=menu_name)
    
    token = request.headers.get("Authorization").split(" ")[1]
    user_id = jwt.decode(token, "SECRET", algorithms=["HS256"])['user_id']
    user = User.objects.filter(id=user_id).first()
    
    user.my_menu.add(menu)
    return Response(status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def add_mystore(request):
    store_name = request.data["store_name"]
    store = get_object_or_404(Restaurant, store_name=store_name)
    
    token = request.headers.get("Authorization").split(" ")[1]
    user_id = jwt.decode(token, "SECRET", algorithms=["HS256"])['user_id']
    user = User.objects.filter(id=user_id).first()
    
    user.my_store.add(store)
    return Response(status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def delete_mymenu(request):
    menu_name = request.data["menu_name"]
    menu = get_object_or_404(Menu, menu_name=menu_name)
    
    token = request.headers.get("Authorization").split(" ")[1]
    user_id = jwt.decode(token, "SECRET", algorithms=["HS256"])['user_id']
    user = User.objects.filter(id=user_id).first()
    
    user.my_menu.remove(menu)
    return Response(status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def delete_mystore(request):
    store_name = request.data["store_name"]
    store = get_object_or_404(Restaurant, store_name=store_name)
    
    token = request.headers.get("Authorization").split(" ")[1]
    user_id = jwt.decode(token, "SECRET", algorithms=["HS256"])['user_id']
    user = User.objects.filter(id=user_id).first()
    
    user.my_store.remove(store)
    return Response(status.HTTP_204_NO_CONTENT)

@api_view(["GET"])
def show_mymenu(request):
     # 발급해준 토큰이 request 형태로 들어온다, 그것을 token에 담아주고,
     token = request.headers.get("Authorization").split(" ")[1]
     # jwt decoder를 통해서 토큰에 담긴 정보를 가져오는데, 우리가 필요한건 유저 정보니까 User_id만 가져온다.
     user_id = jwt.decode(token, "SECRET", algorithms=["HS256"])['user_id']
     # user_id(pk)를 통해서 유저 객체를 찾는다.
     user = User.objects.filter(id=user_id).first()
     my_menu = user.my_menu.all()
     serializer = MenuSerializer(my_menu, many=True)
     return Response(serializer.data)

@api_view(["GET"])
def show_mystore(request):
     # 발급해준 토큰이 request 형태로 들어온다, 그것을 token에 담아주고,
     token = request.headers.get("Authorization").split(" ")[1]
     # jwt decoder를 통해서 토큰에 담긴 정보를 가져오는데, 우리가 필요한건 유저 정보니까 User_id만 가져온다.
     user_id = jwt.decode(token, "SECRET", algorithms=["HS256"])['user_id']
     # user_id(pk)를 통해서 유저 객체를 찾는다.
     user = User.objects.filter(id=user_id).first()
     my_stores = user.my_store.all()
     serializer = RestaurantSerializer(my_stores, many=True)
     return Response(serializer.data)