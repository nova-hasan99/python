from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name="Student Name")
    roll = models.IntegerField(unique=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
