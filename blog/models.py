from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments',)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])