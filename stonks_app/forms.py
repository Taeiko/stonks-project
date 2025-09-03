from django import forms
from .models import Stock
from django.contrib.auth.models import User

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock 
        fields = ['name', 'amount', 'purchase_date', 'purchase_price','current_price' ]

        widgets = {
            'purchase_date': forms.DateInput(attrs={'type':'date'})
        }

class SignUpForm (forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']