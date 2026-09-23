from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CONDITION_CHOICES = [
        ('new', 'New'),
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('fair', 'Fair'),
    ]

    SIZE_CHOICES = [
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        ('FREE', 'Free Size'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    brand = models.CharField(max_length=100,blank=True)
    size = models.CharField(max_length=10,choices=SIZE_CHOICES)
    condition = models.CharField(max_length=20,choices=CONDITION_CHOICES)
    stock = models.PositiveIntegerField(default=1)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='products/')
    alt_text = models.CharField(max_length=200,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.product.name} Image"

    