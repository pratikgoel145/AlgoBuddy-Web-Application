from django.contrib import admin
from .models import Post, Comment, Markread

admin.site.register(Post)

admin.site.register(Comment)

admin.site.register(Markread)

# admin.site.register(Profile)