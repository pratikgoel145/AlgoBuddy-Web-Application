from django.core.urlresolvers import reverse
from django.db import models


class User(models.Model):
   name = models.CharField(max_length=30, null=False)
   username = models.CharField(max_length=30, unique=True)
   password = models.CharField(max_length=30, null=False)
   progress = models.PositiveIntegerField(default=0)

   def get_absolute_url(self):
      return reverse('con')

   def __str__(self):
       return self.username

