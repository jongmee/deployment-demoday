from rest_framework import serializers
from .models import Menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     qs = qs.filter(post__pk=self.kwargs["post_pk"])
    #     return qs