#  Ilya  Odnoral, Pizza  calculator
while True:
    try:
        hoeveelheid_klein =int(input('Hoeveel small pizza\'s wilt u?'))
        break
    except ValueError:
        print('Dit is geen heel nummer!')
        continue
while True:
    try:      
        hoeveelheid_medium= int(input('Hoeveel medium pizza\'s wilt u?'))
        break
    except ValueError:
        print('Dit is geen heel nummer!')
        continue
while  True:
    try:
        hoeveelheid_grooot = int(input('Hoeveel groot pizza\'s wilt u?'))
        break    
    except ValueError:
        print("Dit is geen heel nummer!")
        continue
getaal1  = hoeveelheid_klein * 6.50
getaal2 =  hoeveelheid_medium * 9.30
getaal3 = hoeveelheid_grooot * 11.10
betallen  = getaal3  + getaal1 + getaal2
print('**********************KASSA BON**********************')
print(f'Pizza\'s small         {hoeveelheid_klein} x 6.50  =      {round(getaal1, 3)}')
print(f'Pizza\'s medium        {hoeveelheid_medium} x 9.30  =     {round(getaal2, 3)}')
print(f'Pizza\'s large         {hoeveelheid_grooot} x 11.10 =     {round(getaal3, 3)}')
print('----------------------------------------------------')
print(f'Te betallen:                    {round(betallen, 2)}')
