from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import DailyReport, ExercisePlan, MealPlan, Consultation
from .serializers import UserSerializer, DailyReportSerializer, ExercisePlanSerializer, MealPlanSerializer, ConsultationSerializer

def home(request):
    """View สำหรับหน้าหลัก"""
    return render(request, 'home.html') # render template ชื่อ home.html

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DailyReportViewSet(viewsets.ModelViewSet):
    queryset = DailyReport.objects.all()
    serializer_class = DailyReportSerializer

    @action(detail=False, methods=['get'])
    def my_reports(self, request):
        """endpoint สำหรับดึงรายงานประจำวันของผู้ใช้ปัจจุบัน"""
        reports = DailyReport.objects.filter(user=request.user)
        serializer = DailyReportSerializer(reports, many=True)
        return Response(serializer.data)

class ExercisePlanViewSet(viewsets.ModelViewSet):
    queryset = ExercisePlan.objects.all()
    serializer_class = ExercisePlanSerializer

class MealPlanViewSet(viewsets.ModelViewSet):
    queryset = MealPlan.objects.all()
    serializer_class = MealPlanSerializer

class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer   