from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .models import TopicInformation, TopicCategory
from .forms import NewUserForm, EditProfileForm


def homepage(request):
    return render(request, "main/home.html",
                  {"information": TopicInformation.objects.all, "category": TopicCategory.objects.all})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request=request,
                          template_name="main/register.html",
                          context={"form": form})

    form = NewUserForm
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


def edit(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.info(request, f"You have successfully updated your profile")
            return redirect("main:homepage")
        else:
            form = EditProfileForm(instance=request.user)
            return render(request=request,
                          template_name="main/edit.html",
                          context={"form": form})
    else:
        form = EditProfileForm(instance=request.user)
        return render(request=request,
                      template_name="main/edit.html",
                      context={"form": form})







