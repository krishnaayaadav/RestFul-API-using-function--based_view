from django.db import models

# Create your models here.

class Student(models.Model):
    name  =  models.CharField(max_length=77)
    email =  models.EmailField()
    age   =  models.PositiveIntegerField()
    stu_id=  models.PositiveIntegerField()