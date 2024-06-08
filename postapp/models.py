from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    userid = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=30)
    birthdate = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')], null=True, blank=True)
    is_korean = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'userid'
    REQUIRED_FIELDS = ['username', 'email']

    def __str__(self):
        return self.username