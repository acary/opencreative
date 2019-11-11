from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from playlists import views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path("blog/", include("blog.urls")),
    path("posts/", include("blog.urls")),
    path('contact/', views.contact, name='contact'),
    path("feed/", include("feed.urls")),
    path("playlists/", include("playlists.urls")),
    path("products/", include("products.urls")),
    path('projects/', include('projects.urls')),
    path("social/", include("social.urls")),
    path('thanks/', views.thanks, name='thanks'),
    # AUTH
    path("accounts/", include("accounts.urls")),
    path('accounts/', include('django.contrib.auth.urls')), # new
    path('video/search', views.video_search, name='video_search'),
    # Functions
    path('discover/', views.discover, name='discover'),
    path('create/', views.create, name='create'),
    path('publish/', views.publish, name='publish'),
    path('track/', views.track, name='track'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
