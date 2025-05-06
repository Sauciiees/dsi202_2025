# /myproject/myapp/urls.py
from django.urls import path
from .views import (
    home, plans, chat , RentBikeView,dashboard,
    BikeListCreateAPIView, BikeRetrieveUpdateAPIView,
)
from . import views

urlpatterns = [
    # Existing frontend URLs
    path('', home, name='home'),
    path('plans/', plans, name='plans'),
    path('chat/', chat, name='chat'),
    path('api/chat/', views.chat_with_openrouter, name='chat_with_openrouter'),
    
   
   
]