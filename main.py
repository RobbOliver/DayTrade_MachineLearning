
if __name__ == "__main__":
    from iqoptionapi.stable_api import IQ_Option
    from multiprocessing import Process
    import pandas as pd
    import time

    # Conexão com a IQ OPTION
    mail = input('Email: ')
    passwd = input('Senha: ')

    I_want_money = IQ_Option(mail, passwd)
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


    sleepTo(5)


    # Main program
    # GET PROGRAM

