from django import forms
from .models import Stock

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock 
        fields = ['name', 'amount', 'purchase_date', 'purchase_price','current_price' ]