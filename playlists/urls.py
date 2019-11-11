from django.contrib import auth, admin
from django.contrib.auth import views as auth_views # Intermediate course
from django.urls import include, path
from django.contrib.auth import views # Intermediate course
from django.conf.urls import include, url, static
from django.conf import settings
from . import views
from . import models

urlpatterns = [
    path('', views.playlists, name="playlists"), # This is Playlists

    path('home/', views.home, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    # Playlist
    path('playlist/create/',views.CreatePlaylist.as_view(), name="create_playlist"),
    path('playlist/<int:pk>/',views.DetailPlaylist.as_view(), name='detail_playlist'),
    path('playlist/<int:pk>/update/',views.UpdatePlaylist.as_view(template_name='update_playlist.html'), name='update_playlist'),
    path('playlist/<int:pk>/delete/',views.DeletePlaylist.as_view(template_name='delete_playlist.html'), name='delete_playlist'),
    # Video
    path('playlist/<int:pk>/addvideo', views.add_video, name='add_video'),
    path('playlist/<int:pk>/upvote', views.playlist_upvote, name='playlist_upvote'),
    path('video/<int:pk>/delete', views.DeleteVideo.as_view(template_name='delete_video.html'), name='delete_video'),
]
