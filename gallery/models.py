from django.db import models

from django.contrib.auth.models import User

class Photo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_photos', blank=True)
    tags = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()
