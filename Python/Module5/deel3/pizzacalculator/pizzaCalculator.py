from Functions_van_mij import input_check

pizza_prijs = {'small': 6.50, 'medium': 9.30, 'large': 11.10, 'extra large': 15}
keys_sort = list(pizza_prijs.keys())



def kies():
    hoeveelheden = {}
    # hoeveelheden = {'small': 0, 'medium': 0, 'large': 0, 'extra large: 0}
    while True:
        size = input_check('Welke size wilt u kopen? (small/medium/large/extra large): ', str, ['small', 'medium', 'large', 'extra large'])
        hoeveelheid = input_check('Hoeveel?', int, [])
        print(hoeveelheid)
        if size in hoeveelheden:
            print('hoi')
            hoeveelheden[size] += hoeveelheid
        else:
            print('hoi2')
            hoeveelheden[size] = hoeveelheid
        print(hoeveelheden)
        doorgaan = input_check('Wilt u doorgaan met nog een pizza? (ja/nee): ', str, ['ja', 'nee']).lower()
        if doorgaan == 'nee':
            break
    return hoeveelheden

hoeveelheden = kies()

print('**********************KASSA BON**********************')
total = 0

for size in hoeveelheden:
    prijs = pizza_prijs[size]
    total += hoeveelheden[size] * prijs
for size in hoeveelheden:
    if hoeveelheden[size]:
        print(f'Pizza\'s {size:10}  {hoeveelheden[size]:3.0f} x {pizza_prijs[size]:8.2f}  =  {hoeveelheden[size] * pizza_prijs[size]:8.2f}')

print('----------------------------------------------------')
print(f'                         Te betalen: {total:10.2f}')
