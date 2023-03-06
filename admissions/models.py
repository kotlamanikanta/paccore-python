from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    fathername = models.CharField(max_length=20)
    classname = models.IntegerField(null=True)
    contact = models.IntegerField(max_length=10)
 