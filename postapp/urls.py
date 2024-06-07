from django.contrib import admin
from django.urls import path, include

from postapp.views import hello_world

app_name = "postapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
]
