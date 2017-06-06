from django.contrib.auth.views import (
    login as base_login
)
from django.shortcuts import redirect, render, HttpResponse
from django.utils.translation import ugettext

from .forms import AuthenticationForm, UserCreationForm


def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponse('Successed!')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

def user_login(request):
    return base_login(request, authentication_form=AuthenticationForm, template_name='users/login.html')
