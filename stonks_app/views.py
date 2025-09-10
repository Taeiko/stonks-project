from django.shortcuts import render, redirect
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

class StockListView(ListView):
    model = Stock
    template_name = 'stocks/stock-list.html'
    context_object_name= 'stocks'
    # this function shows current price in my portfolio
    # i used a youtube tutorial to make a function that gets real time stock prices from the finnhub api.
    # youtube tutorial link: https://www.youtube.com/watch?v=Nu3bEtNrmIw
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        api_key = settings.FINNHUB_API_KEY
        # this is to help me explain this better.
        # i made a new list that will store the updated stock info 
        stocks_with_prices = []
        # i looped through each stock i have in my list
        total = 0
        for stock in context['stocks']:
            # this variable fetches the current prices using the stock's TICKER name
            current_price = fetch_stock_price(stock.ticker.upper(), api_key)
            # and stores it in this object
            stock.current_price = current_price
            total += (stock.current_price * stock.amount)
            # which then gets added to the new list 
            stocks_with_prices.append(stock)
            # ....that will replace the old list
        context['stocks'] = stocks_with_prices
        print(total)
        context['total'] = total
        # new updated list is shown on the page 
        
        
        return context
    
    def get_queryset(self):
        return Stock.objects.filter(user = self.request.user)
    

from django.contrib.auth.decorators import login_required

def stock_detail(request):
    stocks = Stock.objects.all()
    return render (request, 'stock-details.html', {'stocks': stocks})

@login_required
def stock_create(request):
    if request.method == 'POST':
        form = StockForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            stock = form.save()
            return redirect(reverse("stock_list"))
    else:
        form = StockForm()
        return render(request, "stocks/stock-form.html", {'form': form})


# i used the same function and tutorial i mentioned above to do the same thing here as well.
class StockDetailView(DetailView):
    model = Stock
    template_name = 'stocks/stock-details.html'
    context_object_name = 'stock'
    # this also shows the current price in the details page 
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        api_key = settings.FINNHUB_API_KEY
        stock = context['stock']
        
        stock.current_price = (fetch_stock_price(stock.ticker.upper(), api_key))
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
from django.contrib.auth.models import User
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
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data['c']
