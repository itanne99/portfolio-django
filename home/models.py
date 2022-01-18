from django.db import models


# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    image = models.CharField(max_length=256)
