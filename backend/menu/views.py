from django.shortcuts import render
from .models import Menu, Sale
from .serializers import MenuSerializer, SaleSerializer
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()

class SaleListAPIView(ListAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    
class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(restaurant__pk=self.kwargs["restaurant_pk"])
        return qs


class AllMenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SaleMenuViewSet(ModelViewSet):
    queryset = Menu.objects.exclude(sale=None)
    serializer_class = MenuSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        today = datetime.now().date()
        for query in qs:
            if today < query.sale.start_date:
                qs = qs.exclude(sale=query.sale)
            elif today > query.sale.end_date:
                query.delete()
        return qs


@api_view(["GET"])
def show_mymenu(request):
     user = request.user
     my_menu = user.my_menu.all()
     serializer = MenuSerializer(my_menu, many=True)
     return Response(serializer.data)
