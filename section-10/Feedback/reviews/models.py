from django.db import models

# Create your models here.
class Review(models.Model):
    user_name = models.CharField(max_length=100)
    Review_text= models.TextField()
    rating = models.IntegerField()