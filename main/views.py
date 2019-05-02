from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .models import TopicInformation, TopicCategory


def homepage(request):
    return render(request, "main/home.html",
                  {"information": TopicInformation.objects.all, "category": TopicCategory.objects.all})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            human = True
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request=request,
                          template_name="main/register.html",
                          context={"form": form})

    form = UserCreationForm()
    return render(request=request,
                  template_name="main/register.html",
                  context={"form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password!")
        messages.error(request, "Invalid username or password!")

    form = AuthenticationForm()
    return render(request,
                  "main/login.html",
                  {"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect("main:homepage")