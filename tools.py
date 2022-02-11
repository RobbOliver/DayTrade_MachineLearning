from calendar import timegm
import configparser
import mailbox
from iqoptionapi.stable_api import IQ_Option
from time import time

# Init IQ OPTION --------------

login_aqr = configparser.RawConfigParser()
login_aqr.read('..\..\iql.txt')

mail = login_aqr.get('LOGIN', 'email')
passwd = login_aqr.get('LOGIN', 'passwd')

iqapi = IQ_Option(mail, passwd)
check, reason = iqapi.connect()
if check is False:
    print(f'ERROR: {reason}')
    quit()
else: print('[Done]')

# Settings default
iqapi.change_balance('PRACTICE')  # PRACTICE / REAL



# Func to System --------------

def sleepTo(s, show=True): 
    while True:
        showHr = time.localtime(time.time())
        if showHr[5] == s:
            return True
        else:
            if show is True:
                print(f'[{showHr[5]}]', end='\r')
            else:
                pass
            time.sleep(1)

# Func to IQ OPTION --------------

par = 'EURUSD'
entrada = 2
direcao = 'call'
timeframe = 1

def buyBi():
    status,id = iqapi.buy(entrada, par, direcao, timeframe)
    if status is True:
        print(iqapi.check_win_v4(id))

def sellBi():
    direcao = 'put'
    status, id = iqapi.buy(entrada, par, direcao, timeframe)
    if status is True:
        print(iqapi.check_win_v4(id))
