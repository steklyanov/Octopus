from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

api_router = DefaultRouter()
api_router.register(r'board', DashboardView, 'board')


app_name = 'dashboard'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('agency/<pk>/bookers/', BookerListCreateView.as_view(), name='booker_list'),
    path('agency/<pk>/', AgencyEditView.as_view(), name='agency_edit'),
    path('agency/<pk>/bookers/<booker_id>/', BookerEditView.as_view(), name='booker_edit'),
]
