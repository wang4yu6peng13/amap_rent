#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from urlparse import urljoin
import requests
import csv

url = "http://bj.58.com/pinpaigongyu/pn/{page}/?minprice=0_2500"

#已完成的页数序号，初时为0
page = 0

