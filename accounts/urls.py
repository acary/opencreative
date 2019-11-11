from django.urls import include, path
from django.contrib import auth
from django.contrib.auth import views as auth_views # Intermediate course
from django.contrib.auth import views # Intermediate course
from django.conf.urls import url, include
from . import views

urlpatterns = [
    #path('sign_up/', views.sign_up, name='sign_up'),
    #path('login/', views.login, name='login'),
    #path('logout/', views.logout, name='logout'),
    # AUTH
    path('sign_up/', views.SignUp.as_view(), name='sign_up'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='login')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
