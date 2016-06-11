# coding:utf-8
import sys, urllib, urllib2, json

url = 'http://apis.baidu.com/apistore/stockservice/stock?list=2'


req = urllib2.Request(url)

req.add_header("apikey", "528abcd6d751ccb5196d57558f211ad1")

resp = urllib2.urlopen(req)
content = resp.read()
if(content):
        print(content)

