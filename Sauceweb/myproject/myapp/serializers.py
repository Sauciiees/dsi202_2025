# health_app/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Diary, ExercisePlan, MealPlan, Consultation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class DiarySerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Nested serializer เพื่อแสดงข้อมูลผู้ใช้
    class Meta:
        model = Diary
        fields = '__all__'

class ExercisePlanSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = ExercisePlan
        fields = '__all__'

class MealPlanSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = MealPlan
        fields = '__all__'

class ConsultationSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Consultation
        fields = '__all__'