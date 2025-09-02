from django.shortcuts import render

# Create your views here.
# these are the pages that get displayed when the user types the url
def welcome(request):
    return render(request, 'welcome.html')

from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView
from .models import Stock
from .forms import StockForm

class StockCreateView(CreateView):
    model = Stock
    form_class = StockForm
    template_name = 'stocks/stock-form.html'

class StockListView(ListView):
    model = Stock
    template_name = 'stocks/stock-list.html'
    context_object_name= 'stock'
