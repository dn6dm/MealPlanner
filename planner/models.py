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

    def print(self):
        print("%s: %d %d %d %d" % (self.name, self.calories, self.carbs, self.fat, self.protein))


class FoodPlan(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    food_plan = ArrayField(models.CharField(max_length=50), default=list)

    '''def __str__(self):
        return self.food_plan'''

    def create(self, user):
        self.profile = user.profile
        food_items = FoodItem.objects.all()
        calories_left = user.profile.calories
        carbs_left = user.profile.carbs
        fat_left = user.profile.fat
        protein_left = user.profile.protein
        for i in food_items:
            if calories_left - i.calories >= -50 and carbs_left - i.carbs >= -5 and fat_left - i.fat >= -5:
                self.food_plan.append(i.name)
                calories_left = calories_left - i.calories
                carbs_left = carbs_left - i.carbs
                fat_left = fat_left - i.fat
                protein_left = protein_left - i.protein
            if calories_left < 70:
                break
        '''if calories_left < 70:
            self.save()
        else:
            pass'''

    def print(self):
        total_calories = 0
        total_carbs = 0
        total_fat = 0
        total_protein = 0
        for item in self.food_plan:
            tmp = FoodItem.objects.filter(name=item).first()
            print('%s %d %d %d %d' % (tmp.name, tmp.calories, tmp.carbs, tmp.fat, tmp.protein))
            total_calories += tmp.calories
            total_carbs += tmp.carbs
            total_fat += tmp.fat
            total_protein += tmp.protein
        print('Total %d %d %d %d' % (total_calories, total_carbs, total_fat, total_protein))

    def items(self):
        items_list = {}
        for i in self.food_plan:
            tmp = FoodItem.objects.filter(name=i).first()
            items_list[i] = tmp
        return items_list
