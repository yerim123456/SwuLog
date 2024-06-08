from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accountapp.forms import CustomUserCreationForm
from accountapp.models import CustomUser


# Create your views here.
def hello_world(request):
    return render(request, 'accountapp/hello_world.html')

class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

    def form_valid(self, form):
        return super().form_valid(form)
        return response