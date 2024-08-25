from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    age = models.IntegerField()
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    published_date = models.DateField(auto_now_add=True)
    groups = models.ManyToManyField('auth.Group', related_name='account_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='account_permissions', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
