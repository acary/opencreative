from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Social

def social(request):
    users = Social.objects.all()
    return render(request, "social/users.html", {'users': users})
