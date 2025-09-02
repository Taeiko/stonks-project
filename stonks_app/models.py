from django.db import models
# Create your models here.

class Stock(models.Model):
    name= models.CharField(max_length=80)
    amount = models.BigIntegerField()
    purchase_date = models.DateField('stock purchase date')
    purchase_price = models.DecimalField(decimal_places=2, max_digits=10)
    current_price = models.DecimalField(decimal_places=2, max_digits=10)

