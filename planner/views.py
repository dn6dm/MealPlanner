from django.views.generic.base import TemplateView
from django.contrib import messages
from .forms import FoodItemForm
from django.shortcuts import render, redirect


# Create your views here.

class HomePage(TemplateView):
    template_name = 'planner/home.html'


def add_food(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your food item has been added!')
            return redirect('create_plans')
    else:
        form = FoodItemForm()

    context = {
        'form': form
    }

    return render(request, 'planner/create_plans.html', context)
