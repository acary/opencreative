from django.http import Http404
from django.http import JsonResponse
from django.contrib import auth
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, HttpResponseRedirect #
from django.template import loader #
from django.urls import path, include, reverse
from django.db.models import Count
from feed.models import Highlight
from projects.models import Project
from blog.models import Post
from playlists.models import Playlist
from products.models import Product
from feed.views import highlight_index
from django.forms.utils import ErrorList
from django.contrib.auth import views
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import urllib
import requests
from .forms import SearchForm

YOUTUBE_API_KEY = 'AIzaSyDGKbpAdwZH4idxUnV4ssevfcau7ArtwJU'

def index(request):
    posts = Highlight.objects.all().order_by('-created_on')
    projects = Project.objects.all()
    context = {
        'posts': posts,
        'projects': projects,
    }
    return render(request, 'index.html', context)

def discover(request):
    posts = Highlight.objects.all().order_by('-created_on')
    projects = Project.objects.all()
    context = {
        'posts': posts,
        'projects': projects,
    }
    return render(request, 'discover.html', context)

def create(request):
    posts = Highlight.objects.all().order_by('-created_on')
    projects = Project.objects.all()
    context = {
        "posts": posts,
        'projects': projects,
    }
    return render(request, 'create.html', context)

def publish(request):
    posts = Highlight.objects.all().order_by('-created_on')
    projects = Project.objects.all()
    context = {
        'posts': posts,
        'projects': projects,
    }
    return render(request, 'publish.html', context)

def track(request):
    projects = Project.objects.all().count()
    users = User.objects.all().count()
    playlists = Playlist.objects.all().count()
    products = Product.objects.all().count()
    posts = Post.objects.all().count()
    highlights = Highlight.objects.all().count()
    context = {
        'posts': posts,
        'projects': projects,
        'users': users,
        'playlists': playlists,
        'products': products,
        'posts': posts,
        'highlights': highlights,
    }
    return render(request, 'track.html', context)

def about(request):
    posts = Highlight.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, 'about.html', context)

def contact(request):
    return render(request, 'contact.html', {})

def thanks(request):
    correspondence = request.GET['message']
    wordlist = correspondence.split()
    return render(request, 'thanks.html', {'correspondence': correspondence, 'wordlist': len(wordlist)})

@login_required
def video_search(request):
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        encoded_search_term = urllib.parse.quote(search_form.cleaned_data['search_term'])
        response = requests.get(f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=6&q={ encoded_search_term }&key={ YOUTUBE_API_KEY }')
        return JsonResponse(response.json())
    return JsonResponse({'error':'Not able to validate form'})

# Note that once we’ve done this in all these views, we no longer need to import loader and HttpResponse (you’ll want to keep HttpResponse if you still have the stub methods for detail, results, and vote).
#
# The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. It returns an HttpResponse object of the given template rendered with the given context.
#
# https://docs.djangoproject.com/en/2.1/intro/tutorial03/
