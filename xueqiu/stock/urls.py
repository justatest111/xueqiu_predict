from django.conf.urls import patterns, include, url  
from views import StockListView
  
urlpatterns = patterns('',  
    # Examples:  
    url(r'^$',StockListView.as_view(), name = 'index'), 
)  