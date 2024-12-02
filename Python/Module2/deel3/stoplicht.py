import time 
from termcolor import colored, cprint, COLORS
while True:
    a = 3
    for i in range (1,3):
       
        print(colored(f'*** {a}', 'red'))
        a-=1
        time.sleep(1)
    b = 10
    for i in range (1,1):
        print(colored(f'*** {b}','yellow'))
        b-=1
        time.sleep(1)
    c = 20
    for i in range (1,2):
         print(colored(f'*** {c}','green'))
         c-=1
         time.sleep(1)
    b = 10
    for i in range (1,1):
         print(colored(f'*** {b}','yellow'))
         b-=1
         time.sleep(1)
    
