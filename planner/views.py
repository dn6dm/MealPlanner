from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib import messages
from .forms import FoodItemForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import FoodPlan, FoodItem
from django.views.generic import ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


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
        plan.save(user=request.user)
        plan.create()
        messages.success(request, f'Your plan has been created!')
        return redirect('display_plans', plan.id)
    return render(request, 'planner/create_plans.html')


class PlanListView(ListView):
    model = FoodItem
    context_object_name = "plan_items"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = self.kwargs['pk']
        return context

    '''def get_queryset(self):
        return FoodPlan.objects.get(id=self.kwargs['pk']).plan_items.get_queryset()'''

    '''def post(self, request, *args, **kwargs):
        plan = request.session.get("created_plan", None)
        plan.save()
        messages.success(request, f'Your plan has been saved!')
        context = {
            'items_list': request.session.get("created_plan", None)
        }
        return render(request, 'planner/fooditem_list.html', context)'''


class PlanDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = FoodPlan
    success_url = '/'

    def test_func(self):
        plan = self.get_object()
        if self.request.user.profile == plan.profile:
            return True
        return False

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(request, f'Your plan was deleted')
        return super(PlanDeleteView, self).delete(request, *args, **kwargs)


class ProfilePlanListView(ListView):
    model = FoodPlan
    template_name = 'planner/profile_plans.html'
    context_object_name = 'plans'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        profile = user.profile
        return FoodPlan.objects.filter(profile=profile)
