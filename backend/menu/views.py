from django.shortcuts import render
from .models import Menu
from .serializers import MenuSerializer
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

import random

class MenuListAPIView(ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(restaurant__pk=self.kwargs["restaurant_pk"])
        return qs


# class RandomMenuListAPIView(ListAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer

#     def get_queryset(self):
#         qs = super().get_queryset()
#         print(type(qs))
#         return qs

# @api_view(["GET"])
# def random_menu(request):
#     random_list = []
#     querys = Menu.objects.all()
#     querys = list(querys)
#     # print(querys)
#     for i in range(3):
#         random_num = random.randrange(0, len(querys))
#         random_list.append(querys[random_num])
#         del querys[random_num]

#     print(random_list)


#     return Response(status.HTTP_204_NO_CONTENT)