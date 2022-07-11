from tkinter import CASCADE
from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=20)

class Car(models.Model):
    name = models.CharField(max_length=20)
    brand = models.ForeignKey(Brand, on_delete=CASCADE)