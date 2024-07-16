"""
Models
"""

from django.db import models

# Create your models here.
class Person(models.Model):
    """
    Person class
    """
    name = models.CharField(max_length=100)
    age = models.IntegerField()
