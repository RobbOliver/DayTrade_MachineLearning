from time import time

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