from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from core.models import Actor, Client, Job, Booker, Agency
from core.serializers import AgencySerializer, BookerSerializer
from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet
from django.core import serializers
from rest_framework import generics


# class DashboardView(generics.RetrieveUpdateDestroyAPIView):
class DashboardView(generics.ListAPIView):
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAuthenticated, )   #  , IsAdminUser
    serializer_class = BookerSerializer

    def get_queryset(self):
        booker = Booker.objects.get(user_id=self.request.user.id)
        print(booker.agency_id)
        return Booker.objects.all()


class AgencyEditView(generics.ListAPIView):
    # queryset = Agency.objects.all()
    serializer_class = AgencySerializer

    def get_queryset(self, *args, **kwargs):
        """" Return a default options """
        id = self.kwargs['pk']
        object = Agency.objects.filter(id=id)

        return object