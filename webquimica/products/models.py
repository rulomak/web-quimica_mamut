
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)

    def __str__(self):
        return self.name





class Product(models.Model):
    title = models.CharField(max_length=120, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="products")
    updated = models.DateTimeField(auto_now=True)
    price = models.FloatField(null=True, blank=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.title



