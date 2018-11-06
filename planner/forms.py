from django import forms
from .models import FoodItem, FoodPlan


class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'calories', 'carbs', 'fat', 'protein', 'serving_size']
