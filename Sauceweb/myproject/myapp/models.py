from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Diary(models.Model):
    meal = models.CharField(max_length=100)
    food = models.CharField(max_length=100 )
    calories = models.IntegerField()
    exercise = models.IntegerField(default=0)

class Workout(models.Model):
    title = models.CharField(max_length=100)  # Example field
    image = models.ImageField(upload_to='', blank=True, null=True)
    description = models.CharField(max_length=300)  # Example field

class ExercisePlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise_type = models.CharField(max_length=100)
    intensity_level = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    frequency_per_week = models.IntegerField()

    def __str__(self):
        return f"Exercise Plan for {self.user.username} - {self.exercise_type}"

class MealPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.CharField(max_length=100)
    carbohydrates_g = models.FloatField()
    fat_g = models.FloatField()
    protein_g = models.FloatField()
    fiber_g = models.FloatField()
    calories = models.IntegerField()

    def __str__(self):
        return f"Meal Plan for {self.user.username} - {self.food}"

class Consultation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    consultation_type = models.CharField(max_length=100) # 'physical' หรือ 'mental'
    symptoms = models.TextField()
    duration = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    severity_level = models.CharField(max_length=100)

    def __str__(self):
        return f"Consultation for {self.user.username} - {self.consultation_type}"
    
class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    date_logged = models.DateField(default=timezone.now)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.calories} kcal) on {self.date_logged}"