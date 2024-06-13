from django.urls import path

from postapp import views
from searchapp.views import api_search

app_name = 'searchapp'

urlpatterns = [
    path('api_search', api_search, name='api_search'),
]