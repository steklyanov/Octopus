from django.urls import path, include
from .views import BookerPageView

urlpatterns = [
    path('booker/', BookerPageView.as_view()),
]
