from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from core.models import Actor, Client, Job, Booker, Agency
from core.serializers import AgencySerializer, BookerSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.core import serializers
from rest_framework import generics


class DashboardView(generics.ListAPIView):
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer


class AgencyEditView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Agency.objects.all()
    serializer_class = AgencySerializer

    def get_queryset(self, *args, **kwargs):
        """" Return a default options """
        print("qqqqqqqq", self.kwargs)

        id = self.kwargs['pk']
        object = Agency.objects.filter(id=id)

        return object