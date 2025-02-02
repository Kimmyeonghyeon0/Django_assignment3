from django.conf import settings
from config import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as django_login
from django.shortcuts import render, redirect


def sign_up(request):
#     username = request.POST.get('username')
#     password1 = request.POST.get('password1')
#     password2 = request.POST.get('password2')
#
#
#     print('username', username)
#     print('password1', password1)
#     print('password2', password2)

    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(settings.LOGIN_URL)

    context = {
        'form': form
    }

    return render(request, 'registration/signup.html', context)


def login(request):
    form = AuthenticationForm(request, request.POST or None)
    if form.is_valid():
        django_login(request, form.get_user())
        from django.urls import reverse
        return redirect(reverse('blog_list'))
    else:
        form = AuthenticationForm(request)

    context = {
        'form': form
    }
    return render(request, 'registration/login.html', context)