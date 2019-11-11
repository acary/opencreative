from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime,now

class Playlist(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    sort_order = models.IntegerField(default=1)
    votes_total = models.IntegerField(default=1)
    pub_date = models.DateTimeField(default=datetime.now)
    commentary = models.TextField(max_length=999, blank=True)

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    youtube_id = models.CharField(max_length=255)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    description = models.TextField(max_length=999, blank=True)
    author_comment = models.TextField(max_length=999, blank=True)
    pub_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
