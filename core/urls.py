from django.urls import path, include
from .views import BookerProfileView

app_name = 'octopus'

urlpatterns = [
    path('booker_profile/', BookerProfileView.as_view(), name='booker_profile'),
    path('booker_list/', BookerProfileView.as_view(), name='booker_list')
]
