from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}".title()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    description = models.TextField()
    favorite = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="category")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.author}"

