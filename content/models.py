from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
   title = models.CharField(max_length=100)
   body = models.TextField(default="")
   code = models.TextField(default="")
   images = models.FileField()
   activeusers = set()

   def get_absolute_url(self):
      return reverse('inside')

   def __str__(self):
       return self.title


class Markread(models.Model):
   post = models.ForeignKey(Post, related_name='markread')
   user = models.CharField(max_length=100)

   def __str__(self):
       return self.user


class Comment(models.Model):
   post = models.ForeignKey(Post, related_name='comments')
   user = models.CharField(max_length=100)
   body = models.TextField()
   created = models.DateTimeField(auto_now_add=True)

   class Meta:
       ordering = ['-created']

   def __str__(self):
       return self.user
