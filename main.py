from iqoptionapi.stable_api import IQ_Option
# from time import sleep
import pandas as pd
import time

# Conexão com a IQ OPTION
I_want_money = IQ_Option("email", "password")
check, reason = I_want_money.connect()
if check is False:
    print(f'ERROR: {reason}')
    quit()

# Settings default
I_want_money.change_balance('PRACTICE')  # PRACTICE / REAL


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


sleepTo(0)

while True:
    end_from_time = time.time()
    lista_result = []
    dif = 0.00008

    # Main program
    # GET PROGRAM
    data = I_want_money.get_candles("EURUSD", 60, 10, end_from_time)
    data = pd.DataFrame(data)

    # LIST RESULT
    for i in range(10):
        try:
            if data['close'][i] < data['close'][i+5]:
                if data['close'][i] + dif < data['close'][i+5]:
                    lista_result.append(4)
                else:
                    lista_result.append(3)

            if data['close'][i] > data['close'][i+5]:
                if data['close'][i] - dif > data['close'][i+5]:
                    lista_result.append(2)
                else:
                    lista_result.append(1)

        except Exception:
            lista_result.append(-1)

    # DO_

    showHr = time.localtime(time.time())
    if showHr[5] >= 12:
        if lista_result[0] != 4 and lista_result[1] == 4:
            status, id = I_want_money.buy(3, 'EURUSD', 'call', 1)
            sleepTo(59, False)

    # sleepTo(59, False)

    print(lista_result[:-5], showHr[5], end='\r')
