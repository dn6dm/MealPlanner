from django.views.generic.base import TemplateView
from django.contrib import messages
from .forms import FoodItemForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import FoodPlan


# Create your views here.

class HomePage(TemplateView):
    template_name = 'planner/home.html'


def add_food(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your food item has been added!')
            return redirect('add_foods')
    else:
        form = FoodItemForm()

    context = {
        'form': form
    }

    return render(request, 'planner/add_foods.html', context)


@login_required
def create_plan(request):
    if request.method == 'POST':
        plan = FoodPlan()
        plan.create(user=request.user)
        plan.save()
        messages.success(request, f'Your plan has been created!')
    return render(request, 'planner/create_plans.html')
