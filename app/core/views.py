from django.shortcuts import render
from rest_framework import generics
from .serializers import ActorSerializer, BookerSerializer
from .models import Actor, Booker

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import get_user_model
# Create your views here.


class BookerProfileView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    serializer_class = BookerSerializer

    def get_object(self):
        """ Show user only own tasks """
        user_id = self.request.user.id
        # print(user)
        return Booker.objects.get(user_id=user_id)


class BookerActorsListView(generics.ListAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    serializer_class = ActorSerializer

    def get_queryset(self):
        if not self.request.user.is_anonymous:
            booker = Booker.objects.get(user_id=self.request.user)
            queryset_list = Actor.objects.filter(agency__id=booker.agency.id)
            return queryset_list
