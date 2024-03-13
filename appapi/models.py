from django.db import models

# Create your models here.
class TeachersModel(models.Model):
    id = models.AutoField(primary_key=True)
    RegNo = models.IntegerField()
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Phone = models.IntegerField()
    Domian =models.CharField(max_length=100)