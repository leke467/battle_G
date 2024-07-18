from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group, Permission, AbstractUser






class Account(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=100, null=False, blank=False)

    gender = models.CharField(max_length=100)
    published_date = models.DateField(auto_now_add=True)

    groups = models.ManyToManyField(Group, related_name='account_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='account_permissions')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'age', 'country']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

