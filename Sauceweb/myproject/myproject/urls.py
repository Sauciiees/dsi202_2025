# config/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from myapp import views # import view ของเรา
# myproject/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet) # สร้าง endpoint สำหรับ User
router.register(r'daily_reports', views.DiaryViewSet) # สร้าง endpoint สำหรับ DailyReport
router.register(r'exercise_plans', views.ExercisePlanViewSet)
router.register(r'meal_plans', views.MealPlanViewSet)
router.register(r'consultations', views.ConsultationViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/chat/', views.chat_with_openrouter, name='chat_with_openrouter'),
    path('', views.home, name='home'), # เพิ่ม view สำหรับหน้าหลัก
    path('plans/', views.plans, name='plans'), # เพิ่ม view สำหรับหน้าหลัก
    path('chat/', views.chat, name='chat'), # เพิ่ม view สำหรับหน้าหลัก
    path('user/', views.user, name='user'),
    path('workout/', views.workout, name='workout'),
    path('accounts/', include('allauth.urls')), # URL สำหรับ allauth
    path('plans/delete/<Diary_food>', views.delete),
    path('promptpay/', views.promptpay_payment, name='promptpay_payment'),
    path('package/', views.package, name='package'),
    
     
    
    

   
   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)