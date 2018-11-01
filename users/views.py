from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from .forms import UserForm


def subscriber_new(request, template='users/user_new/html'):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            return HttpResponseRedirect('/success/')
        else:
            form = UserForm()
        return render(request, template, {'form': form})
