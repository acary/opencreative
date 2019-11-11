from django.db import models
from django.utils.timezone import datetime,now

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)
    pub_date = models.DateTimeField(default=datetime.now)
    categories = models.ManyToManyField('Category', related_name='projects')

    def __str__(self):
        return self.title
