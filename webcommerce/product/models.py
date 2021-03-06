from django.db import models
from category.models import Category

class Rating(models.Model):
    name =  models.CharField(max_length=120)
    description = models.TextField() 

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='product_pics')
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, default=None, null=True)
    
    def __str__(self):
        return f'{self.title} Category: {self.category}'
 
