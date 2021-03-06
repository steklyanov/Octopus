
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from djoser.serializers import UserCreateSerializer
from core.models import Actor, Client, Job, Booker, Agency
from core.serializers import AgencySerializer, BookerSerializer
from rest_framework import generics


# class DashboardView(generics.RetrieveUpdateDestroyAPIView):
class DashboardView(generics.ListCreateAPIView):
    """ Show all agencies """
    serializer_class = AgencySerializer

    def get_queryset(self):
        return Agency.objects.all()


# class BookerListCreateView(generics.ListCreateAPIView):
#     """ Create or show all bookers of the selected agency """
#     serializer_class = BookerSerializer
#
#     def get_queryset(self, *args, **kwargs):
#         id = self.kwargs['pk']
#         booker = Booker.objects.filter(agency_id=id)
#
#         return booker


class BookerListCreateView(generics.ListCreateAPIView):
    """ Create or show all bookers of the selected agency """
    serializer_class = BookerSerializer

    def get_queryset(self, *args, **kwargs):
        id = self.kwargs['pk']
        booker = Booker.objects.filter(agency_id=id)

        return booker


class BookerEditView(generics.RetrieveUpdateDestroyAPIView):
    """Edit selected agency data"""
    serializer_class = BookerSerializer

    def get_queryset(self, *args, **kwargs):
        print(*args)
        print(*kwargs)
        id = self.kwargs['booker_id']
        booker = Booker.objects.filter(id=id)

        return booker


class AgencyEditView(generics.RetrieveUpdateDestroyAPIView):
    """Edit selected agency data"""
    serializer_class = AgencySerializer

    def get_queryset(self, *args, **kwargs):
        id = self.kwargs['pk']
        agency = Agency.objects.filter(id=id)

        return agency
