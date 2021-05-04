#перевод бабосов с киви
#qiwi hack
#bili
# SimpleQIWI
from SimpleQIWI import *
import os
def pay():
    token=input('токен: ')
    phone=input('номер: ')
#part 1
    os.system('clear')
    api=QApi(token=token, phone=phone)
    print('[+]номер ',phone)
    print('[+]токен ',token)
    print('[$]баланс ',api.balance[0],' рублей')
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

pay()
