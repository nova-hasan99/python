from django.db import models

class BookStoreModel(models.Model):
    CATEGORY = (
        ('Horror', 'Horror'),
        ('Thiller', 'Thiller'),
        ('Novel', 'Novel'),
    )
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category  = models.CharField(max_length=50, choices=CATEGORY)
    first_pub = models.DateTimeField(auto_now_add=True)
    last_pub = models.DateTimeField(auto_now=True)
