from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email_address = models.EmailField()
    

class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=100)
    image_name = models.ImageField()
    data = models.DateField()
    slug = models.SlugField()
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
class Tag(models.Model):
    caption = models.CharField(max_length=50)
    posts= models.ManyToManyField(Post)
    