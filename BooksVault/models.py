from django.contrib.auth.models import AbstractUser
from django.db import models
from .choices import CATEGORIES

class User(AbstractUser):
    pass

class Authors(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="authors", null=True)
    name = models.CharField(max_length=255)
    biography = models.TextField()
    
class Publisher(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="publisher", null=True)
    name = models.CharField(max_length=255)
    
class Book(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="books", null=False)
    name = models.CharField(max_length=64, null=False)
    ISBN = models.CharField(max_length=13, null=False)
    category = models.CharField(choices=CATEGORIES, max_length=10, null=True, blank=True)
    image_url = models.URLField(null=False)
    authors = models.ManyToManyField(Authors)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, related_name="books_published")
    added_at = models.DateTimeField(auto_now_add=True, null=True) 
        
    def __str__(self):
        return f"Name: {self.name}, ISBN: {self.ISBN}"

class List(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=64, null=False)
    books = models.ManyToManyField(Book)