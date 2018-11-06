from django.db import models
from users.models import Profile
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class FoodItem(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    calories = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
    serving_size = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class FoodPlan(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    food_plan = ArrayField(models.CharField(max_length=50), default=list)

    def create(self, user):
        self.profile = user.profile
        food_items = FoodItem.objects.all()
        calories_left = user.profile.calories
        carbs_left = user.profile.carbs
        fat_left = user.profile.fat
        protein_left = user.profile.protein
        for i in food_items:
            if calories_left - i.calories >= 0 and carbs_left - i.carbs >= 0 and fat_left - i.fat >= 0:
                self.food_plan.append(i.name)
                calories_left = calories_left - i.calories
                carbs_left = carbs_left - i.carbs
                fat_left = fat_left - i.fat
                protein_left = protein_left - i.protein
            if calories_left < 100:
                break
        self.save()
