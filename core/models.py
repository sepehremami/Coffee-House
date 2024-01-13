from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class Order(models.Model):
    class Status(models.TextChoices):
        confirmed = "c", "confirmed"
        nconfirmed = "n", "not confirmed"

    title = models.CharField(max_length=30)
    status = models.CharField(max_length=1, choices=Status)
