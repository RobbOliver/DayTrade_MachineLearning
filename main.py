from iqoptionapi.stable_api import IQ_Option
from tools import sleepTo
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


# Main program
# GET PROGRAM

