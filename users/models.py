from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    carbs = models.IntegerField(default=206)
    fat = models.IntegerField(default=67)
    protein = models.IntegerField(default=146)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()
