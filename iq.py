import time
from iqoptionapi.stable_api import IQ_Option
Iq=IQ_Option("robsoncaetano667@gmail.com","137200")
goal="EURUSD"
print("get candles")
print(Iq.get_candles(goal,60,111,time.time()))