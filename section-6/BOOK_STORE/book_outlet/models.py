from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Country(models.Model):
    country = models.CharField(max_length=50)
    codr= models.CharField(max_length=2)
    
    class Meta:
        verbose_name_plural = "Countries"
        
    def __str__(self):
        return self.country
        


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city=models.CharField(max_length=50)
    
    def full_address(self):
        return f"{self.street}, {self.postal_code}, {self.city}."
    
    def __str__(self):
        return self.full_address()
    
    class Meta:
        verbose_name_plural = "Address Entries"


class Author(models.Model):
    first_name= models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
    
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()


class books(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="related_books")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True)
    published_countries = models.ManyToManyField(Country)
    # db_index basically help in finding data faster.
    # when we use any field offen to retrive data we should consider adding db_index there.
    
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
        
    
    def __str__(self):
        return f"{self.title} ({self.rating})"
    