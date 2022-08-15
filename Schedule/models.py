from django.db import models
from django.contrib.auth.models import User


class Data(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)    
    categoria = models.CharField(max_length=200)
    profissional = models.CharField(max_length=200)
    data = models.CharField(max_length=200)