from django.urls import path, include
from .views import *


app_name = 'dashboard'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('agency/<pk>/', AgencyEditView.as_view(), name='agency_edit')

]