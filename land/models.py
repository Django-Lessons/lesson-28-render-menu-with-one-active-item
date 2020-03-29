from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Document(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('review', 'Reviewed'),
        ('ready', 'Ready'),
    )

    title = models.CharField(max_length=30)
    private = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=16)
