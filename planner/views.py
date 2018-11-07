from django.views.generic.base import TemplateView
from django.contrib import messages
from .forms import FoodItemForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import FoodPlan, FoodItem
from django.views.generic import ListView


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
        items_list = {}
        for i in plan.food_plan:
            tmp = FoodItem.objects.filter(name=i).first()
            items_list[i] = tmp
        messages.success(request, f'Your plan has been created!')
        return render(request, 'planner/display_plans.html', {'items_list': items_list, 'plan': plan})
    return render(request, 'planner/create_plans.html')


class PlanListView(ListView):
    model = FoodItem
    template_name = 'planner/display_plans.html'
    context_object_name = 'items_list'

    '''def get_queryset(self):
        return FoodPlan.objects.last().items()'''

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            pass