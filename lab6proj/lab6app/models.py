from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    # Other fields as needed

class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course, related_name='students')
    # Other fields as needed

# Create your models here.
