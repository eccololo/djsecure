from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    return render(request, template_name="index.html")

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("two_factor:login")
    context = {"form": form}
    return render(request, template_name="register.html", context=context)

@login_required(login_url="two_factor:login")
def dashboard(request):
    return render(request, template_name="dashboard.html")

def user_logout(request):
    auth.logout(request)
    messages.success(request, "Logout success!")
    return redirect("home")


def account_locked(request):
    return render(request, template_name="account-locked.html")