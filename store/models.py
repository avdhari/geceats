from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Food(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name