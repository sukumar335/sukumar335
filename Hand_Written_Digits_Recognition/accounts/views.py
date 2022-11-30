from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.urls import reverse

from .forms import LoginForm, RegisterForm


User = get_user_model()

# Create your views here.
def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        try:
            user = User.objects.create_user(username, email, password)
        except:
            user = None
        if user != None:
            return HttpResponseRedirect(reverse('accounts:login'))
    context = {
        "form": form
    }
    return render(request, "accounts/registration.html", context)

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return HttpResponseRedirect(reverse('app:home-view'))
    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))