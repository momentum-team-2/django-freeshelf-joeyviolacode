from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from users.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True)

    def __str__(self):
        return f"{self.name}".title()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    url = models.CharField(max_length=255, unique=True)
    image_url = models.CharField(max_length=1023, null=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="books")
    date_added = models.DateTimeField(auto_now_add=True)
    favorited_by = models.ManyToManyField(User, related_name="favorite_books")
    fave_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} - {self.author}"

class Comment(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="comments")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"by {self.author} about {self.book} on {self.date_added}"
