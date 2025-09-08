from django.shortcuts import render
from django.conf import settings
import requests
import os

# Create your views here.
# these are the pages that get displayed when the user types the url
def welcome(request):
    return render(request, 'welcome.html')

from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Stock
from .forms import StockForm

class StockCreateView(CreateView):
    model = Stock
    form_class = StockForm
    template_name = 'stocks/stock-form.html'
    success_url = reverse_lazy('stock_list')

class StockListView(ListView):
    model = Stock
    template_name = 'stocks/stock-list.html'
    context_object_name= 'stocks'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        print(context['stocks'][0].total_earning)
        return context

# to show the current price of the stock 
def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    api_key = os.getenv(settings.FINNHUB_API_KEY)
    
    stocks_with_prices = []
    for stock in context['stocks']:
        current_price = fetch_stock_price(stock.name.upper(), api_key)
        stock.current_price = current_price
        stocks_with_prices.append(stock)
    
    context['stocks'] = stocks_with_prices
    return context

class StockDetailView(DetailView):
    model = Stock
    template_name = 'stocks/stock-details.html'
    context_object_name = 'stock'
    # this also shows it in the details page 
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        api_key = settings.FINNHUB_API_KEY
        
        stock = context['stock']
        
        print('name',stock.ticker.upper())
        stock.current_price = (fetch_stock_price(stock.ticker.upper(), api_key))
        print(stock.current_price)
        context['current_price'] = stock.current_price
        return context

class StockUpdateView(UpdateView):
    model = Stock
    form_class = StockForm
    template_name = 'stocks/stock-form.html'
    
    def get_success_url(self):
        return reverse("stock_details", kwargs={"pk": self.object.pk})


class StockdeleteView(DeleteView):
    model = Stock
    template_name = 'stocks/stock_confirm_delete.html'
    success_url = reverse_lazy("stock_list")




# the stuff for login and signup and whatever 
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'registration/sign-up.html'

class SignInView(LoginView):
    model = User
    template_name = 'registration/login.html'
    authentication_form = AuthenticationForm
    success_url = reverse_lazy("welcome")



# this will get the current price of the stock
def fetch_stock_price(symbol,api_key):
    url = f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={api_key}'
    print(url)
    response = requests.get(url)
    print(response.json())
    response.raise_for_status()
    data = response.json()
    print(data)
    return data['c']


# # this will calculate the total profit gained from all the stocks owned using the amount of stocks owned and the current price of each stock 
# def calculate_profit():
    