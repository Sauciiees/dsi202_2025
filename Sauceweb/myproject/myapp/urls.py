# /myproject/myapp/urls.py
from django.urls import path
from .views import (
    home, plans, BikeDetailView, RentBikeView,dashboard,
    BikeListCreateAPIView, BikeRetrieveUpdateAPIView,
)

urlpatterns = [
    # Existing frontend URLs
    path('', home, name='home'),
    path('plans/', plans, name='plans')
]