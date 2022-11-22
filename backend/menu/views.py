from django.shortcuts import render
from .models import Menu, Sale
from .serializers import MenuSerializer, SaleSerializer
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from datetime import datetime

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
