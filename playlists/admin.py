from django.contrib import admin
from .models import Playlist, Video

class PlaylistAdmin(admin.ModelAdmin):
    name = 'playlist'

admin.site.register(Playlist,PlaylistAdmin)
admin.site.register(Video)
