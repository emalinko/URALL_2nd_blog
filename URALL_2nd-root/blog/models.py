from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=140)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    image = models.ImageField(upload_to='blog_images/%Y/%m/%d/')