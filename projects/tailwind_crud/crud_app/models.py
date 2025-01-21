from django.db import models
import os

def student_directory_name(instance, filename):
    return os.path.join('student/', instance.name, filename)
class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    image = models.ImageField(upload_to=student_directory_name, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"