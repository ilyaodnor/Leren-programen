from Functions_van_mij import input_check

pizza_prijs = {'small': 6.50, 'medium': 9.30, 'large': 11.10}

def kies():
    hoeveelheden = {'small': 0, 'medium': 0, 'large': 0}
    lijst = []
    
    while True:
        size = input_check('Welke size wilt u kopen?(small/medium/groot)?', str)
        if size in pizza_prijs and size not in lijst:
            lijst.append(size)
            hoeveelheden[size] += 1
        else:
            print('Voer een geldige size in (klein/medium/groot)!')
        
        if input('Wilt u doorgaan? (ja/nee): ').lower() == 'nee':
            break
    
    return hoeveelheden

hoeveelheden = kies()

print('**********************KASSA BON**********************')
for size in pizza_prijs:
    if hoeveelheden[size] > 0:
        print(f'Pizza\'s {size}         {hoeveelheden[size]} x {pizza_prijs[size]}  = {round(hoeveelheden[size] * pizza_prijs[size], 2)}')

total = sum(hoeveelheden[size] * pizza_prijs[size] for size in pizza_prijs)
print('----------------------------------------------------')
print(f'Te betallen:                    {round(total, 2)}')
