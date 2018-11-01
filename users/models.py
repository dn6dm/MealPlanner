from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    carbs = models.IntegerField()
    fat = models.IntegerField()
    protein = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()
