import requests
from bs4 import BeautifulSoup
import json


#def crawl_stocks_name():
#    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
#            'Host':'xueqiu.com',
#                    'Upgrade-Insecure-Requests': 1,
#                    'Accept-Encoding': 'gzip, deflate, sdch',
#                    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6'}
#                    # 'Cookie':'s=2rfd15xt45; __utma=1.1446861734.1464484351.1464484351.1464484351.1; __utmb=1.1.10.1464484351; __utmc=1; __utmz=1.1464484351.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); webp=1; _sid=eW8ckI9yjHgIR6fQHFVDQ3DfBlBa6O; bid=06518b3a2bf1fd756abb42fd5d8d68da_iorwe6kz; xq_a_token=934f674c5167ef0a40bc92c387554e5b8d74a6f8; xq_r_token=ed5549c6fd48ab1fbe3f40b00a823b21dbd4f618; Hm_lvt_1db88642e346389874251b5a1eded6e3=1464167262,1464484373,1464484468,1464484475; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1464484731'}
#    for page_num in range(1,2):
#        get_list_result = requests.get("https://xueqiu.com/hq#exchange=CN&firstName=1&secondName=1_0&page="+str(page_num), headers=headers)
#        raw_list = BeautifulSoup(get_list_result.content, 'html.parser')
#       # print get_list_result
#        print raw_list.find_all("a")

def crawl_stocks_name():
#    raw_stocks_list = requests.get("http://ctxalgo.com/api/stocks",headers=headers)
    raw_stocks_list = requests.get("http://ctxalgo.com/api/stocks")
    print raw_stocks_list
    stocks_list = json.loads(raw_stocks_list.content)
 #   print stocks_list
    
    for i in stocks_list:
        print  i
        print stocks_list[i]
    

crawl_stocks_name()


