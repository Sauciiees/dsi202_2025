# /myproject/myapp/urls.py
from django.urls import path
from .views import (
    home, plans, chat , user,entBikeView,dashboard,
    BikeListCreateAPIView, BikeRetrieveUpdateAPIView,
)
from . import views

urlpatterns = [
    # Existing frontend URLs
    path('', home, name='home'),
    path('plans/', views.plans, name='plans'),
    path('chat/', chat, name='chat'),
    path('user/', user, name='user'),
    path('api/chat/', views.chat_with_openrouter, name='chat_with_openrouter'),
    
    
   
   
]