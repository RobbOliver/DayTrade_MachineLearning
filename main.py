if __name__ == "__main__":
    from iqoptionapi.stable_api import IQ_Option
    from multiprocessing import Process
    import pandas as pd
    import time

mail = input('\n Email: ')
passwd = input('Password: ')

I_want_money = IQ_Option(mail, passwd)
check, reason = I_want_money.connect()
if check is False:
    print(f'ERROR: {reason}')
    quit()
else: print('[Done]')

# Settings default
I_want_money.change_balance('PRACTICE')  # PRACTICE / REAL

# Main program
# GET PROGRAM