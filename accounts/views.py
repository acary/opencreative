from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import views as auth_views # Intermediate course
from django.contrib.auth import authenticate # Intermediate course
from django.contrib.auth import login as auth_login # Intermediate course
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth import views # Intermediate course
from django.urls import reverse, reverse_lazy # Class-based views auth
from django.views import generic # Class-based views auth
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('index')
    template_name = 'accounts/sign_up.html'

    def form_valid(self, form):
        view = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'),form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        auth_login(self.request, user)
        return view

def sign_up(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/sign_up.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home') #
        else:
            return render(request, "accounts/sign_up.html", {'error':'Passwords must match'})
    else:
        return render(request, 'accounts/sign_up.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('products')
        else:
            return render(request, 'accounts/login.html', {'error':'Username or password is incorrect.'})
    else:
        return render(request, "accounts/login.html")

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('products')

# def home(request):
#     return render(request, "products/home.html")
