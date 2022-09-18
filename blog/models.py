from tkinter import CASCADE
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return self.full_name()





class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    img = models.ImageField(upload_to='blog-img', height_field=None, width_field=None, max_length=None, blank=True)
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True,db_index=True, unique=True, null=False)
    content = models.TextField()
    tags = models.ManyToManyField("blog.Tag")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
        
    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("blog_specific", args=[self.slug])
    
    def __str__(self):
        return f'{self.title} {self.date}'

class Comment(models.Model):
    email = models.EmailField(max_length=254)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    comment_text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Tag(models.Model):
    caption = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.caption}'