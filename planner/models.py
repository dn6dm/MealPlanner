from django.db import models
from users.models import Profile


# Create your models here.
class FoodItem(models.Model):
    name = models.CharField(max_length=50)
    calories = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class FoodPlan(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    fooditems = models.ManyToManyField(FoodItem)
    calories = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
