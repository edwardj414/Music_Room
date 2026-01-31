from django.contrib.auth.models import AbstractUser
from django.db import models

class CusUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    code = models.CharField(max_length=10, blank=True, null=True)
    is_host = models.BooleanField(default=False)
    def __str__(self):
        return self.username