from django.db import models

# Create your models here.
def default_details():
    return {}

class Product(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300, blank=True)
    details = models.JSONField(default=default_details)
    category = models.CharField(max_length=30)
    tags = models.TextField(default='')
    price= models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/products/')

    def __str__(self):
        return self.name