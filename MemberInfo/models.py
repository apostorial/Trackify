from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MemberInfo(models.Model):

    GOALS = [
        ('Lose weight', 'Lose weight'),
        ('Maintain weight', 'Maintain weight'),
        ('Gain weight', 'Gain weight'),
        ('Gain muscle', 'Gain muscle'),
    ]

    SEXES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    
    ACTIVITY_LEVELS = [
        ('Sedentary', 'Sedentary'),
        ('Lightly active', 'Lightly active'),
        ('Moderately active', 'Moderately active'),
        ('Very  active', 'Very active'),
        ('Extra active', 'Extra active'),
    ]

    member = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    goal = models.CharField(max_length=255, choices=GOALS)
    sex = models.CharField(max_length=255, choices=SEXES)
    age = models.IntegerField(default=18)
    height = models.IntegerField(default=150)
    weight = models.FloatField(default=50)
    weight_goal = models.FloatField(default=50)
    activity_level = models.CharField(max_length=255, choices=ACTIVITY_LEVELS)

    def calculate_bmr(self):
        # Calculates the user's Basal Metabolic Rate (BMR).
        if self.sex == 'Male':
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5
        elif self.sex == 'Female':
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161
        return round(bmr, 2)
    
    def calculate_tdee(self):
        # Calculates the user's Total Daily Energy Expenditure (TDEE).
        bmr = self.calculate_bmr()
        if self.activity_level == "Sedentary":
            tdee = bmr * 1.2
        if self.activity_level == "Lightly active":
            tdee = bmr * 1.375
        if self.activity_level == "Moderately active":
            tdee = bmr * 1.55
        if self.activity_level == "Very active":
            tdee = bmr * 1.725
        if self.activity_level == "Extra active":
            tdee = bmr * 1.9
        return round(tdee, 2)
    
    def calculate_bmi(self):
        height_meters = self.height / 100
        bmi = self.weight / (height_meters ** 2)
        return round(bmi, 2)
    
    def whatShouldIDo(self):
        if self.goal == "Lose weight":
            description = f"Well, considering the fact that you want to {self.goal}, you should focus on reducing your calorie intake. Using the data you provided, your TDEE is {self.calculate_tdee()} kcal. This corresponds to the amount of calories your body burns at your activity level. To lose weight, you'll need to consume fewer calories than your TDEE. We suggest a deficit of around 500 kcal per day. This will help you lose weight at a healthy rate."
        elif self.goal == "Maintain weight":
            description = f"Well, considering the fact that you want to {self.goal}, you should focus on consuming around your TDEE. Using the data you provided, your TDEE is {self.calculate_tdee()} kcal. This is the amount of calories your body burns at your activity level. Maintaining a balanced diet and exercise routine will help you maintain your current weight."
        elif self.goal == "Gain weight":
            description = f"Well, considering the fact that you want to {self.goal}, you should focus on increasing your calorie intake. Using the data you provided, your TDEE is {self.calculate_tdee()} kcal. To gain weight, you'll need to consume more calories than your TDEE. We suggest a surplus of 500-1000 kcal per day. This will help you gain weight at a healthy rate of around a kilogram a week."
        elif self.goal == "Gain muscle":
            description = f"Well, considering the fact that you want to {self.goal}, you should focus on increasing your calorie intake and incorporating strength training exercises. Using the data you provided, your TDEE is {self.calculate_tdee()} kcal. To gain muscle, you'll need to consume a slight surplus of calories and prioritize protein intake. We suggest a surplus of 100-400 kcal per day, with a focus on consuming around 1.5 to 2 gram of protein per kilogram of bodyweight. Strength training exercises will help you build muscle mass."

        return description