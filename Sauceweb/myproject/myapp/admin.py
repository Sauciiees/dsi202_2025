from django.contrib import admin
from .models import Diary, ExercisePlan, MealPlan, Consultation

# Register your models here.
admin.site.register(Diary)
admin.site.register(ExercisePlan)
admin.site.register(MealPlan)
admin.site.register(Consultation)
