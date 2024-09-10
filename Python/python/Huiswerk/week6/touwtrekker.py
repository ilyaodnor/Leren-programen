print('Ilya Odnoral, Touw trekker:')

touw = [3, 4.5, 6.3]
prijzen = {3: 1.23, 4.5: 2.45, 6.3: 4.10}

print('Prijzen per meter voor elke dikte: \n1.  3 cm  = 1.23$\n2.  4.5 cm  = 2.45$\n1.  6.3 cm  = 3.  4.10$\n')
while True:
    try:
        
        touw_pers = float(input('Maak een keuz uit 3 touw diktes :   (3, 4.5, 6.3)'))
        
        if touw_pers not in touw:
            print('Voer in een goeie diktes!')
            continue


        hoeveelheid  = int(input('Hoe veel?'))

        lengete = float(input('Voer in het lengte van het touw(in m):  '))
        break


    
    except ValueError:
        print('Voer een geldig getal in!')
if touw_pers == 3:
    prijs = touw_pers  * 1.23* lengete * hoeveelheid
elif touw_pers== 4.5:
    prijs = touw_pers  * 2.45* lengete * hoeveelheid
elif touw_pers  == 6.3:
    prijs = touw_pers * 4.10* lengete * hoeveelheid
print(f'-----------------------------------')
print(f' Touw {touw_pers}cm dikte, \n x{hoeveelheid}  st \n Met{lengete}m lengte:    \n                        {prijs}$ ')
print(f'-----------------------------------')
