from django.core.exceptions import ObjectDoesNotExist
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
        if 'generate' in request.POST:
            if request.session.get('id', default=None) == None:
                plan = FoodPlan()
                plan.initiate(user=request.user, name=request.POST.get('name'))
                request.session['id'] = plan.id
            else:
                plan = FoodPlan.objects.get(id=request.session.get('id'))
            plan.create()
            messages.success(request, f'Your plan has been created!')
            request.session.pop('id')
            return redirect('display_plans', plan.id)
        elif 'add_food' in request.POST:
            if request.session.get('id', default=None) == None:
                plan = FoodPlan()
                plan.initiate(user=request.user, name=request.POST.get('name'))
                request.session['id'] = plan.id
            else:
                plan = FoodPlan.objects.get(id=request.session.get('id'))
            try:
                plan.add_food(request.POST.get('food_text'))
                plan.save()
                messages.success(request, f'Food item added to plan')
            except ObjectDoesNotExist:
                messages.success(request, f'Food item not found in database')
            return render(request, 'planner/create_plans.html')
    return render(request, 'planner/create_plans.html')


class PlanListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = FoodItem
    context_object_name = "plan_items"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = self.kwargs['pk']
        context['plan'] = FoodPlan.objects.get(id=self.kwargs['pk'])
        return context

    def get_queryset(self):
        return FoodPlan.objects.get(id=self.kwargs['pk']).plan_items.get_queryset()

    def test_func(self):
        plan = FoodPlan.objects.get(id=self.kwargs['pk'])
        if self.request.user.profile == plan.profile:
            return True
        return False

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
        request.session.pop('id', None)
        return super(PlanDeleteView, self).delete(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = self.kwargs['pk']
        return context


class ProfilePlanListView( LoginRequiredMixin, ListView):
    model = FoodPlan
    template_name = 'planner/profile_plans.html'
    context_object_name = 'plans'

    def get_queryset(self):
        profile = self.request.user.profile
        return FoodPlan.objects.filter(profile=profile).order_by('pk')
