from Functions_van_mij import input_check

pizza_prijs = {'small': 6.50, 'medium': 9.30, 'large': 11.10}

def kies():
    hoeveelheden = {'small': 0, 'medium': 0, 'large': 0}
    while True:
        size = input_check('Welke size wilt u kopen? (small/medium/large): ', str, ['small', 'medium', 'large'])
        hoeveelheid = input_check('Hoeveel?', int, [])
        hoeveelheden[size] += hoeveelheid
        doorgaan = input_check('Wilt u doorgaan met nog een pizza? (ja/nee): ', str, ['ja', 'nee']).lower()
        if doorgaan == 'nee':
            break
    return hoeveelheden

hoeveelheden = kies()

print('**********************KASSA BON**********************')
total = sum(hoeveelheden[size] * pizza_prijs[size] for size in pizza_prijs if hoeveelheden[size])
for size in pizza_prijs:
    if hoeveelheden[size]:
        print(f'Pizza\'s {size}  {hoeveelheden[size]} x {pizza_prijs[size]:.2f}  = {hoeveelheden[size] * pizza_prijs[size]:.2f}')
print('----------------------------------------------------')
print(f'Te betalen: {total:.2f}')
