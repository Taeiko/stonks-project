from django import forms
from .models import Stock
from .models import User
from django.contrib.auth.forms import UserCreationForm



class StockForm(forms.ModelForm):
    class Meta:
        model = Stock 
        fields = ['name','ticker','amount', 'purchase_date', 'purchase_price','current_price' ]

        widgets = {
            'purchase_date': forms.DateInput(attrs={'type':'date'})
        }

class SignUpForm (UserCreationForm):
    email = forms.CharField(max_length=200, help_text ='Required')
    class Meta:
        model = User
        fields = ['username', 'password']
