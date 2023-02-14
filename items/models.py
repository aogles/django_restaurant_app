from django.db import models

# Create your models here.


class Item(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(..., max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
