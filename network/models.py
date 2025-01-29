from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True
    )
    
    def __str__(self):
        return self.username

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True) 
    likes = models.ManyToManyField(User, blank=True, related_name='liked_posts') 

    def __str__ (self):
        return f"{self.id}: {self.user.username}: {self.content[:30]}: {self.timestamp}"
