import requests
from BeautifulSoup import BeautifulSoup
from models import Stock
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from celery import shared_task,group
import threading
import time
from django.utils import timezone


@shared_task
def getFollower(stock_number):
    numbers = 404
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
                    'Host':'xueqiu.com',
                            'Upgrade-Insecure-Requests': 1,
                            'Accept-Encoding': 'gzip, deflate, sdch',
                            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6'}
                            # 'Cookie':'s=2rfd15xt45; __utma=1.1446861734.1464484351.1464484351.1464484351.1; __utmb=1.1.10.1464484351; __utmc=1; __utmz=1.1464484351.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); webp=1; _sid=eW8ckI9yjHgIR6fQHFVDQ3DfBlBa6O; bid=06518b3a2bf1fd756abb42fd5d8d68da_iorwe6kz; xq_a_token=934f674c5167ef0a40bc92c387554e5b8d74a6f8; xq_r_token=ed5549c6fd48ab1fbe3f40b00a823b21dbd4f618; Hm_lvt_1db88642e346389874251b5a1eded6e3=1464167262,1464484373,1464484468,1464484475; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1464484731'}
        stock = Stock.objects.get(stock_number=stock_number)
        result = requests.get("https://xueqiu.com/S/"+stock_number+"/follows", headers=headers)
        soup = BeautifulSoup(str(result.content))
        spans = soup.findAll('span')
        for span in spans:
            if span.get('class') is None:
                w = span
                numbers =  w.text.split("(")[1].split(")")[0]
    except:
        pass
#      except Exception:
        #  print Exception
        #  numbers = 404
    stock.new_followers_number = int(numbers) - int(stock.followers_number)
    stock.followers_number = int(numbers)
    stock.save()
    print stock.followers_number,stock.name, result, stock.update_time

    


#@periodic_task(run_every=(crontab(hour="9",day_of_week="*")))
@shared_task
def getAllFollowers():
    stocks = Stock.objects.all()
    for stock in stocks:
        getFollower.delay(stock.stock_number)
        #  print stock,stock.followers_number
        print "Done"
    print "All Done"

@shared_task
def getAllFollowers_fast():
    stocks = Stock.objects.all()
    group(getFollower.s(i.stock_number) for i in stocks)()
    print "finished !"
    
