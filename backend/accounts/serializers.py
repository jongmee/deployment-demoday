from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create(username=validated_data["nickname"])
        user.set_password(validated_data["password"])
        user.save()
        return user
    
    class Meta:
        model = User
        fields = ["pk", "nickname", "password"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nickname','password']