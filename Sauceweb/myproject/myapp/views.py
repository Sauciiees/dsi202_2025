from django.shortcuts import render,redirect
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Diary, ExercisePlan, MealPlan, Consultation, Workout
from .serializers import UserSerializer, DiarySerializer, ExercisePlanSerializer, MealPlanSerializer, ConsultationSerializer
import json
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Meal
from django.db.models import Sum
from django.utils import timezone
from allauth.socialaccount.models import SocialAccount
from django.contrib import messages
from .utils import generate_promptpay_qr




def home(request):
    """View สำหรับหน้าหลัก"""
    aggregates = Diary.objects.aggregate(
        total_calories=Sum('calories'),
        total_exercise=Sum('exercise')
    )
    total_calories = aggregates['total_calories'] or 0
    total_exercise = aggregates['total_exercise'] or 0
    net_calories = total_calories - total_exercise
    progress = 320
    goal = 2000
    return render(request, 'home.html',{'progress':progress , 'goal':goal,'net_calories':net_calories , 'total_calories':total_calories,'total_exercise':total_exercise }) # render template ชื่อ home.html

def delete(request,Diary_food):
    diary = Diary.objects.get(food=Diary_food)
    diary.delete()
    messages.success(request, 'Data deleted') # แสดงข้อความเมื่อบันทึกข้อมูลสำเร็จ
    return redirect('/plans') # redirect ไปที่หน้า home หลังจากบันทึกข้อมูลเสร็จ

def plans(request):
    all_diaries = Diary.objects.all() # ดึงข้อมูลทั้งหมดจากโมเดล Diary
    total_calories = Diary.objects.aggregate(total=Sum('calories'))['total'] or 0
    if request.method == 'POST':
        #รับค่าจากฟอร์ม
        meal = request.POST['meal']
        food = request.POST['food']
        calories = request.POST['calories']
        exercise = request.POST['exercise']
        #บันทึกข้อมูลลงฐานข้อมูล
        diary = Diary.objects.create(
            meal=meal,
            food=food,
            calories=calories,
            exercise=exercise
        )
        diary.save()
        messages.success(request, 'Data added') # แสดงข้อความเมื่อบันทึกข้อมูลสำเร็จ
        return redirect('/plans') # redirect ไปที่หน้า home หลังจากบันทึกข้อมูลเสร็จ
    else:
        return render(request, 'plans.html',{'all_diaries':all_diaries , 'total_calories':total_calories}) # render template ชื่อ home.html

def chat(request):
    """View สำหรับหน้าหลัก"""
    return render(request, 'chat.html') # render template ชื่อ home.html

def workout(request):
    """View สำหรับหน้าหลัก"""
    all_workouts = Workout.objects.all() # ดึงข้อมูลทั้งหมดจากโมเดล Workout
    return render(request, 'workout.html' ,{'all_workouts':all_workouts } ) 


def user(request):
    """View สำหรับหน้าหลัก"""
    if request.user.is_authenticated:
        social_account = SocialAccount.objects.filter(user=request.user, provider='google').first()
        profile_picture = social_account.extra_data.get('picture') if social_account else None
        # Show profile/dashboard for logged-in user
        return render(request, 'profile.html', {'user': request.user ,'profile_picture': profile_picture })
    else:
        return render(request, 'user.html') # render template ชื่อ home.html
    
def package(request):
    
   
    return render(request, 'package.html' ) 
    
def promptpay_payment(request):
    # เบอร์โทรศัพท์คงที่ (เปลี่ยนเป็นเบอร์ของคุณ)
    PROMPTPAY_PHONE = '0969496560'
    
    # รับจำนวนเงินจาก request (อาจมาจาก form หรือ parameter)
    amount = float(request.GET.get('amount', 0))
    
    # สร้าง QR Code
    qr_img = generate_promptpay_qr(PROMPTPAY_PHONE, amount)
    
    context = {
        'qr_code': qr_img,
        'amount': amount,
        'phone_number': PROMPTPAY_PHONE
    }
    
    return render(request, 'prompt_pay.html', context)



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DiaryViewSet(viewsets.ModelViewSet):
    queryset =Diary.objects.all()
    serializer_class = DiarySerializer

    @action(detail=False, methods=['get'])
    def my_reports(self, request):
        """endpoint สำหรับดึงรายงานประจำวันของผู้ใช้ปัจจุบัน"""
        reports = Diary.objects.filter(user=request.user)
        serializer = DiarySerializer(reports, many=True)
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
    





