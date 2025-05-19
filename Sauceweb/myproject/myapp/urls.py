# /myproject/myapp/urls.py
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    home, plans, chat , user,delete, workout,
    BikeListCreateAPIView, BikeRetrieveUpdateAPIView,
)
from . import views

urlpatterns = [
    # Existing frontend URLs
    path('', home, name='home'),
    path('plans/', plans, name='plans'),
    path('chat/', chat, name='chat'),
    path('user/', user, name='user'),
    path('workout/', workout, name='workout'),
    path('api/chat/', views.chat_with_openrouter, name='chat_with_openrouter'),
    path('plans/delete/<Diary_food>', delete),
    path('promptpay/', views.promptpay_payment, name='promptpay_payment'),
    path('package/', views.package, name='package'),
    
    
   
   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)