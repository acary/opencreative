from django.db import models

class Highlight(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=100)
    detail = models.TextField()
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.caption
