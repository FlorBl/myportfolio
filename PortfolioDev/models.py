# Create your models here.
from django.db import models

class Visitor(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=150)

    
    def __str__(self):
        return f"{self.name}"
    