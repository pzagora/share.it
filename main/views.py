from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import NewUserForm
# Create your views here.


def homepage(request):
    return render(request, "main/home.html")


def register(request):
    form = UserCreationForm
    return render(request,
                  "main/register.html",
                  {"form": form})
