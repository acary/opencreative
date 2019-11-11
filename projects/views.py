from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404, JsonResponse
from django.urls import reverse_lazy # Class-based views auth
from django.views import generic # Class-based views auth
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from projects.models import Project
# from .forms import VideoForm, SearchForm
from django.contrib.auth import views
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.forms.utils import ErrorList
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import urllib
import requests

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    #project = Project.objects.get(pk=pk)
    project = get_object_or_404(Project.objects, pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

@login_required(login_url="/accounts/sign_up")
def project_upvote(request, pk, *args, **kwargs):
    if request.method == 'POST':
        project = get_object_or_404(Project, pk=pk)
        project.votes_total += 1
        project.save()
        context = {
            'project': project
        }
        return render(request, 'project_detail.html', context)
    else:
        return redirect('/')
