from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name=models.CharField(max_length=200, null=True)
    email=models.EmailField(unique=True, null=True)
    bio=models.TextField(null=True)
    avatar=models.ImageField(null=True, default="avatar.svg")
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]


class Topic(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic=models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name=models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)
    participants=models.ManyToManyField(User, related_name='participants', blank=True)
    updated= models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-updated','-created']

def __str__(self):
    return self.name




from django.db import models

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='child_messages', related_query_name='child_message')

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body

class Reply(models.Model):
    message = models.ForeignKey(Message, related_name='replies', related_query_name='reply', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    reply = models.TextField()
    parent_reply = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='child_replies', related_query_name='child_reply')
    
    def __str__(self):
        return self.user.username


