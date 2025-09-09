from django.db import models
# Create your models here.
from django.contrib.auth.models import User








class Stock(models.Model):
    name= models.CharField(max_length=80)
    ticker = models.CharField(max_length=10)
    amount = models.BigIntegerField()
    purchase_date = models.DateField()
    purchase_price = models.DecimalField(decimal_places=2, max_digits=10)
    current_price = models.DecimalField(decimal_places=2, max_digits=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='stocks', null=True)
    @property
    def total_earning(self):
        return self.amount * self.current_price


# 1. add the user as the foreignkey relationship with the stock (done)
# 2. in your view to create a stock add the logged in user as the creator (done)
# 3. logged in user is in self.request.user
# 4. in the template for stock detais use an if block to check if the logged in user is the same as the creator
