from django.db import models
from django.utils import timezone


class Login(models.Model):
    email = models.CharField(max_length=200)
    password = models.TextField()
    login_date = models.DateTimeField(
            default=timezone.now)
