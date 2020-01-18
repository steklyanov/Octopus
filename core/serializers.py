from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *


# class UserCreateSerializer(UserCreateSerializer):
#     class Meta(UserCreateSerializer.Meta):
#         model = Booker
#         fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name')
#
#         def create(self, validated_data):
#             """Nested serializer need to over-ride the create fn to work"""
#             user = Booker.objects.create(**validated_data)
#             user.set_password(validated_data.get("password"))
#             user.save()
#             return user
#
# class CurrentUserSerializer(serializers.ModelSerializer):
#     """The custom serializer which is the end point fot auth/me"""
#
#     class Meta:
#         model = Booker
#         exclude = ['password']
# class BookerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Booker
#         fields = '__all__'


class ActorSerializer(serializers.Serializer):
    class Meta:
        model = Actor
        fields = '__all__'
