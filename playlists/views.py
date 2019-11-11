from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404, JsonResponse
from django.urls import reverse_lazy # Class-based views auth
from django.views import generic # Class-based views auth
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Playlist, Video
from .forms import VideoForm, SearchForm
from django.contrib.auth import views
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.forms.utils import ErrorList
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import urllib
import requests

YOUTUBE_API_KEY = '' # Removed for safety

def playlists(request):
    recent_playlists = Playlist.objects.all().order_by(
        'sort_order'
    )
    context = {
        "recent_playlists": recent_playlists,
    }
    #popular_playlists = [Playlist.objects.get(pk=1),Playlist.objects.get(pk=2),Playlist.objects.get(pk=3)]
    return render(request, 'playlists.html', context)

def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    playlists = Playlist.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'playlists':playlists})

@login_required
def add_video(request, pk):
    form = VideoForm()
    search_form = SearchForm()
    playlist = Playlist.objects.get(pk=pk)
    if not playlist.user == request.user:
        raise Http404
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            video = Video()
            video.playlist = playlist
            video.url = form.cleaned_data['url']
            parsed_url = urllib.parse.urlparse(video.url)
            video_id = urllib.parse.parse_qs(parsed_url.query).get('v')
            if video_id:
                video.youtube_id = video_id[0] #filled_form.cleaned_data['youtube_id']
                response = requests.get(f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={ video_id[0] }&key={YOUTUBE_API_KEY}')
                json = response.json()
                title = json['items'][0]['snippet']['title']
                video.title = title
                video.save()
                return redirect('detail_playlist', pk)
            else:
                errors = form._errors.setdefault('url', ErrorList())
                errors.append('Needs to be a YouTube URL')
    return render(request, 'add_video.html', {'form':form, 'search_form': search_form, 'playlist': playlist})

@login_required(login_url="/accounts/sign_up")
def playlist_upvote(request, pk, *args, **kwargs):
    if request.method == 'POST':
        playlist = get_object_or_404(Playlist, pk=pk)
        playlist.votes_total += 1
        playlist.save()
        return redirect('/playlists/playlist/' + str(pk))
    else:
        return redirect('/')

class CreatePlaylist(generic.CreateView):
    model = Playlist
    fields = ['title']
    template_name = 'create_playlist.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(CreatePlaylist, self).form_valid(form)
        #return HttpResponseRedirect(reverse_lazy('playlists'))
        return redirect('playlists')

class DetailPlaylist(generic.DetailView):
    model = Playlist
    template_name = 'detail_playlist.html'

class UpdatePlaylist(generic.UpdateView):
    model = Playlist
    template_name = 'update_playlist.html'
    fields = ['title']
    success_url = reverse_lazy('dashboard')

class DeletePlaylist(generic.DeleteView):
    model = Playlist
    template_name = 'delete_playlist.html'
    success_url = reverse_lazy('dashboard')

class DeleteVideo(LoginRequiredMixin, generic.DeleteView):
    model = Video
    template_name = 'playlist/delete_video.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        video = super(DeleteVideo, self).get_object()
        if not video.playlist.user == self.request.user:
            raise Http404
        return video
