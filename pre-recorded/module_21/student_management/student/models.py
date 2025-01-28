from django.db import models
import os
from django.contrib.auth.models import User

def student_directory_name(instance, filename):                      # create directory for each seperae student
    return os.path.join('student/media/', instance.name, filename)

class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=10)
    checkbox = models.BooleanField()
    photo = models.ImageField(upload_to=student_directory_name, default=None, null=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)     # for restrictioin user authenticate/only authenticate user create, edit, update, delete 

    def __str__(self):
        return f"{self.name}"