from django.contrib import admin
from django.urls import path, include
from . import views
# these are the urls, where the views pages live, the name is like a key to take us there.
urlpatterns = [
    path('',views.welcome, name='welcome' ),
    path('stocks/create/', views.StockCreateView.as_view(), name='stock_create'),
    path('stocks/portfolio/', views.StockListView.as_view(), name ='stock_list'),
    path('stocks/<int:pk>/details', views.StockDetailView.as_view(), name='stock_details'),
    path('stocks/<int:pk>/edit', views.StockUpdateView.as_view(), name="stock_update"),
    path('stocks/<int:pk>/delete',views.StockdeleteView.as_view(), name='stock_delete')
]
