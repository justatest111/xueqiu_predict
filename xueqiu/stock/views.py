#coding:utf-8
import requests
import json
from BeautifulSoup import BeautifulSoup
from django.shortcuts import render
from django.views.generic.list import ListView  
# Create your views here.
from models import Stock

class StockListView(ListView):
    queryset = Stock.objects.all().order_by("-new_followers_number")
    template_name = 'stock_list.html'
    context_object_name = "stock_list"
    paginate_by = 50
    
       
def crawl_stocks_name():
#    raw_stocks_list = requests.get("http://ctxalgo.com/api/stocks",headers=headers)
    raw_stocks_list = requests.get("http://ctxalgo.com/api/stocks")
    print raw_stocks_list
    stocks_list = json.loads(raw_stocks_list.content)
 #   print stocks_list
    for i in stocks_list:
        find = Stock.objects.filter(stock_number=i).first()
        if not find:
            stock = Stock.objects.create(
                    name = stocks_list[i],
                    stock_number = i
                    )
            stock.save()
            print stock.name,stock.stock_number,stock.id
        else:
            pass

