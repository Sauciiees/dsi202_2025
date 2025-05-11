from django.shortcuts import render,redirect
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import DailyReport, ExercisePlan, MealPlan, Consultation
from .serializers import UserSerializer, DailyReportSerializer, ExercisePlanSerializer, MealPlanSerializer, ConsultationSerializer
import json
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Meal
from django.db.models import Sum
from django.utils import timezone

def home(request):
    """View สำหรับหน้าหลัก"""
    return render(request, 'home.html') # render template ชื่อ home.html

def plans(request):
    """View สำหรับหน้าหลัก"""
    return render(request, 'plans.html') # render template ชื่อ home.html

def chat(request):
    """View สำหรับหน้าหลัก"""
    return render(request, 'chat.html') # render template ชื่อ home.html

def user(request):
    """View สำหรับหน้าหลัก"""
    return render(request, 'user.html') # render template ชื่อ home.html



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

@csrf_exempt  #  <---  Important:  Handle CSRF properly in production!
def chat_with_openrouter(request):
    """
    Handles chat requests by sending the user's message to the OpenRouter API
    and returning the AI's response.
    """
    if request.method == 'POST':
        try:
            # 1. Get the user's message from the request
            data = json.loads(request.body)
            user_message = data.get('message')

            if not user_message:
                return JsonResponse({'error': 'No message provided.'}, status=400)

            # 2. Prepare the request to the OpenRouter API
            headers = {
                'Authorization': f'Bearer {settings.OPENROUTER_API_KEY}',  #  <---  Use your API key from settings.py
                'Content-Type': 'application/json'
            }
            payload = {
                'model': 'deepseek/deepseek-chat:free',  #  <---  Choose your desired model
                'messages': [{'role': 'user', 'content': user_message}]  #  <---  Format the message for OpenRouter
            }

            openrouter_url = 'https://openrouter.ai/api/v1/chat/completions'  #  <---  OpenRouter API endpoint

            # 3. Send the request to OpenRouter
            response = requests.post(openrouter_url, headers=headers, json=payload)
            response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)

            # 4. Process the response from OpenRouter
            ai_response_data = response.json()  #  <---  Parse the JSON response from OpenRouter
            ai_response = ai_response_data['choices'][0]['message']['content']  #  <---  Extract the AI's message

            # 5. Send the AI's response back to chat.html
            return JsonResponse({'response': ai_response})  #  <---  Send the response as JSON

        except requests.exceptions.RequestException as e:
            # Handle network errors (e.g., connection problems, timeout)
            return JsonResponse({'error': f'Error communicating with OpenRouter: {str(e)}'}, status=500)
        except json.JSONDecodeError:
            # Handle errors if the request body from chat.html is not valid JSON
            return JsonResponse({'error': 'Invalid JSON received from frontend.'}, status=400)
        except KeyError:
            # Handle errors if the OpenRouter response doesn't have the expected format
            return JsonResponse({'error': 'Unexpected response format from OpenRouter.'}, status=500)
    else:
        # Handle cases where the request method is not POST (e.g., GET, PUT)
        return JsonResponse({'error': 'Method not allowed.'}, status=405)
    





