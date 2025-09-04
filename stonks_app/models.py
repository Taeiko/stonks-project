from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class Stock(models.Model):
    name= models.CharField(max_length=80)
    amount = models.BigIntegerField()
    purchase_date = models.DateField()
    purchase_price = models.DecimalField(decimal_places=2, max_digits=10)
    current_price = models.DecimalField(decimal_places=2, max_digits=10)



class User(AbstractBaseUser):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


