from django.contrib import admin
from .models import DailyReport, ExercisePlan, MealPlan, Consultation

# Register your models here.
admin.site.register(DailyReport)
admin.site.register(ExercisePlan)
admin.site.register(MealPlan)
admin.site.register(Consultation)
