# admin.py
from django.contrib import admin

from .models import Post, Photo, Like

admin.site.register(Post)
admin.site.register(Photo)
admin.site.register(Like)
