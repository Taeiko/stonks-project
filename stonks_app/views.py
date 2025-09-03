from django.shortcuts import render

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


class StockDetailView(DetailView):
    model = Stock
    template_name = 'stocks/stock-details.html'
    context_object_name = 'stock'


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