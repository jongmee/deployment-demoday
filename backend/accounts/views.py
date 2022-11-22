from .models import Account
from .serializers import AccountSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


import random


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer