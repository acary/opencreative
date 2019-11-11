from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Product(models.Model):
    categories = models.ManyToManyField('Category', related_name='products')
    title = models.CharField(max_length=100)
    url = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body = models.TextField()
    contributor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

class Offer(models.Model):
    categories = models.ManyToManyField('Category', related_name='offers')
    title = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100,default="Curated Box")
    cta_landing = models.CharField(max_length=100,default="Create Your Box")
    url = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body = models.TextField()
    contributor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

class Selection(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    selection = models.ForeignKey('Offer', on_delete=models.CASCADE)

    def __str__(self):
        return self.body
