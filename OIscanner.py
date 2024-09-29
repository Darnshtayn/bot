import ccxt
from time import sleep
import requests

a = False
# Инициализация Binance Futures
exchange = ccxt.binance({
    'options': {
        'defaultType': 'future',  # Указываем, что нас интересуют фьючерсы
    }
})
markets = exchange.fetch_markets()
usdt_pairs = [market['symbol'] for market in markets if market['quote'] == 'USDT']
my_list1 = []
my_list2 = []
my_list3 = []
my_list4 = []
my_list5 = []
my_list6 = []
my_list7 = []
my_list8 = []
my_list9 = []
my_list10 = []
requests.get('https://api.telegram.org/bot5880896601:AAEt_tOoEycSBPQHjXq34NoAOUPSS6CfUCU/sendMessage?chat_id=871112832&text=START')
for symbol in usdt_pairs:
    if ':' in symbol:
        continue

    # Проверяем, поддерживает ли биржа получение открытого интереса
    if exchange.has['fetchOpenInterest']:
        # Получаем открытый интерес для пары
        try:
            open_interest = exchange.fetch_open_interest(symbol)
        except:
            continue

        # Теперь используем корректный ключ 'openInterestAmount'
        if 'openInterestAmount' in open_interest:
            my_list1.append(symbol + ':' + str(open_interest['openInterestAmount']))
            print(symbol)

for symbol in usdt_pairs:
    if ':' in symbol:
        continue

    # Проверяем, поддерживает ли биржа получение открытого интереса
    if exchange.has['fetchOpenInterest']:
        # Получаем открытый интерес для пары
        try:
            open_interest = exchange.fetch_open_interest(symbol)
        except:
            continue

        # Теперь используем корректный ключ 'openInterestAmount'
        if 'openInterestAmount' in open_interest:
            my_list2.append(symbol + ':' + str(open_interest['openInterestAmount']))
            print(symbol)


for symbol in usdt_pairs:
    if ':' in symbol:
        continue

    # Проверяем, поддерживает ли биржа получение открытого интереса
    if exchange.has['fetchOpenInterest']:
        # Получаем открытый интерес для пары
        try:
            open_interest = exchange.fetch_open_interest(symbol)
        except:
            continue

        # Теперь используем корректный ключ 'openInterestAmount'
        if 'openInterestAmount' in open_interest:
            my_list3.append(symbol + ':' + str(open_interest['openInterestAmount']))
            print(symbol)


for symbol in usdt_pairs:
    if ':' in symbol:
        continue

    # Проверяем, поддерживает ли биржа получение открытого интереса
    if exchange.has['fetchOpenInterest']:
        # Получаем открытый интерес для пары
        try:
            open_interest = exchange.fetch_open_interest(symbol)
        except:
            continue

        # Теперь используем корректный ключ 'openInterestAmount'
        if 'openInterestAmount' in open_interest:
            my_list4.append(symbol + ':' + str(open_interest['openInterestAmount']))
            print(symbol)


for symbol in usdt_pairs:
    if ':' in symbol:
        continue

    # Проверяем, поддерживает ли биржа получение открытого интереса
    if exchange.has['fetchOpenInterest']:
        # Получаем открытый интерес для пары
        try:
            open_interest = exchange.fetch_open_interest(symbol)
        except:
            continue

        # Теперь используем корректный ключ 'openInterestAmount'
        if 'openInterestAmount' in open_interest:
            my_list5.append(symbol + ':' + str(open_interest['openInterestAmount']))
            print(symbol)


for symbol in usdt_pairs:
    if ':' in symbol:
        continue

    # Проверяем, поддерживает ли биржа получение открытого интереса
    if exchange.has['fetchOpenInterest']:
        # Получаем открытый интерес для пары
        try:
            open_interest = exchange.fetch_open_interest(symbol)
        except:
            continue

        # Теперь используем корректный ключ 'openInterestAmount'
        if 'openInterestAmount' in open_interest:
            my_list6.append(symbol + ':' + str(open_interest['openInterestAmount']))
            print(symbol)


for symbol in usdt_pairs:
    if ':' in symbol:
        continue

    # Проверяем, поддерживает ли биржа получение открытого интереса
    if exchange.has['fetchOpenInterest']:
        # Получаем открытый интерес для пары
        try:
            open_interest = exchange.fetch_open_interest(symbol)
        except:
            continue

        # Теперь используем корректный ключ 'openInterestAmount'
        if 'openInterestAmount' in open_interest:
            my_list7.append(symbol + ':' + str(open_interest['openInterestAmount']))
            print(symbol)

for symbol in usdt_pairs:
    if ':' in symbol:
        continue

    # Проверяем, поддерживает ли биржа получение открытого интереса
    if exchange.has['fetchOpenInterest']:
        # Получаем открытый интерес для пары
        try:
            open_interest = exchange.fetch_open_interest(symbol)
        except:
            continue

        # Теперь используем корректный ключ 'openInterestAmount'
        if 'openInterestAmount' in open_interest:
            my_list8.append(symbol + ':' + str(open_interest['openInterestAmount']))
            print(symbol)

for symbol in usdt_pairs:
    if ':' in symbol:
        continue

    # Проверяем, поддерживает ли биржа получение открытого интереса
    if exchange.has['fetchOpenInterest']:
        # Получаем открытый интерес для пары
        try:
            open_interest = exchange.fetch_open_interest(symbol)
        except:
            continue

        # Теперь используем корректный ключ 'openInterestAmount'
        if 'openInterestAmount' in open_interest:
            my_list9.append(symbol + ':' + str(open_interest['openInterestAmount']))
            print(symbol)

for symbol in usdt_pairs:
    if ':' in symbol:
        continue

    # Проверяем, поддерживает ли биржа получение открытого интереса
    if exchange.has['fetchOpenInterest']:
        # Получаем открытый интерес для пары
        try:
            open_interest = exchange.fetch_open_interest(symbol)
        except:
            continue

        # Теперь используем корректный ключ 'openInterestAmount'
        if 'openInterestAmount' in open_interest:
            my_list10.append(symbol + ':' + str(open_interest['openInterestAmount']))
            print(symbol)

a1 = my_list1
a2 = my_list2
a3 = my_list3
a4 = my_list4
a5 = my_list5
a6 = my_list6
a7 = my_list7
a8 = my_list8
a9 = my_list9
a10 = my_list10 

while True:
    num = 0
    print('aaaaaaaaaaa')
    requests.get('https://api.telegram.org/bot5880896601:AAEt_tOoEycSBPQHjXq34NoAOUPSS6CfUCU/sendMessage?chat_id=871112832&text=aaaaaa')
    for j in my_list1 :
        if my_list10[num].split(":")[0] != j.split(":")[0]:
            continue
        
        proc = (((float(my_list10[num].split(":")[1])-float(j.split(":")[1]))/float(j.split(":")[1])))*100
        if proc > 3:
            print(num)
            print(proc)
            print(my_list10[num])
            print(j)
            requests.get('https://api.telegram.org/bot5880896601:AAEt_tOoEycSBPQHjXq34NoAOUPSS6CfUCU/sendMessage?chat_id=871112832&text=' + str(proc) + '\n' + str(my_list10[num]) + '\n' + str (j) + '\n' + 'https://www.coinglass.com/tv/Binance_' + j.split(":")[0].replace('/', ''))

        num = num + 1

    my_list1 = a2
    my_list2 = a3
    my_list3 = a4
    my_list4 = a5
    my_list5 = a6
    my_list6 = a7
    my_list7 = a8
    my_list8 = a9
    my_list9 = a10
    for symbol in usdt_pairs:
        if ':' in symbol:
            continue

        # Проверяем, поддерживает ли биржа получение открытого интереса
        if exchange.has['fetchOpenInterest']:
            # Получаем открытый интерес для пары
            try:
                open_interest = exchange.fetch_open_interest(symbol)
            except:
                continue

            # Теперь используем корректный ключ 'openInterestAmount'
            if 'openInterestAmount' in open_interest:
                my_list10.append(symbol + ':' + str(open_interest['openInterestAmount']))
                print(symbol)

    a1 = my_list1
    a2 = my_list2
    a3 = my_list3
    a4 = my_list4
    a5 = my_list5
    a6 = my_list6
    a7 = my_list7
    a8 = my_list8
    a9 = my_list9
    a10 = my_list10








# import ccxt
# from time import sleep
# a = False
# # Инициализация Binance Futures
# exchange = ccxt.binance({
#     'options': {
#         'defaultType': 'future',  # Указываем, что нас интересуют фьючерсы
#     }
# })
# markets = exchange.fetch_markets()
# usdt_pairs = [market['symbol'] for market in markets if market['quote'] == 'USDT']
# my_list = []
# my_list2 = []
# # Выводим все пары с USDT
# print("Пары, торгующиеся с USDT:")
# while True:
#     for pair in usdt_pairs:
#         if ':' in pair:
#             continue
#         symbol = pair

#         # Проверяем, поддерживает ли биржа получение открытого интереса
#         if exchange.has['fetchOpenInterest']:
#             # Получаем открытый интерес для пары
#             try:
#                 open_interest = exchange.fetch_open_interest(symbol)
#             except:
#                 continue

#             # Теперь используем корректный ключ 'openInterestAmount'
#             if 'openInterestAmount' in open_interest:
#                 print(f"{symbol}")
#                 if a:
#                     my_list2.append(symbol + ':' + str(open_interest['openInterestAmount']))
#                     # print(open_interest['openInterestAmount'])
#                 else:
#                     my_list.append(symbol + ':' + str(open_interest['openInterestAmount']))  # Добавляем элемент 4 в конец списка
#                     # print(open_interest['openInterestAmount'])

#     num = 0
#     if a:
#         for j in my_list:
#             if my_list2[0+num].split(":")[0] != j.split(":")[0]:
#                 continue
#             proc = (((float(my_list2[0+num].split(":")[1])-float(j.split(":")[1]))/float(j.split(":")[1])))*100
#             if proc > 5:
#                 print(num)
#                 print(proc)
#                 print(my_list2[0+num])
#                 print(j)
#             num = num + 1
#         my_list = my_list2
#         my_list2 = []
# https://www.coinglass.com/tv/Binance_AEVOUSDT
#     if a == False:
#         a = True
#     sleep(15*60)