from email import message
from operator import mod
from tabnanny import verbose
from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

class Post(models.Model):
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    intro = models.TextField(max_length=200)
    paragraph_one = models.TextField( null=True, blank=True)
    paragraph_two = models.TextField( null=True, blank=True)
    paragraph_three = models.TextField( null=True, blank=True)
    paragraph_four = models.TextField( null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)

    class Meta:
        ordering = ("-created_at",)


    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.name
    
class Subscribers(models.Model):
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    

class MailMessage(models.Model):
    title = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)


    def __str__(self):
        return self.title