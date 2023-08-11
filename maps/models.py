from django.db import models

# Create your models here.

class project(models.Model):
    city_start=models.CharField(max_length=100, null=True)
    city_end=models.CharField(max_length=100, null=True)
    city_between=models.CharField(max_length=100, null=True)
    