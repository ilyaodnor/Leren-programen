from termcolor import colored, cprint, COLORS



croisanten = int(input('hoeveel croisanten wilt u?'))
stokbroden =  int(input('hoeveel  stokbroden'))
kortingsbonnen = int(input('hoeveel koortings bonnen heeft u?'))
if kortingsbonnen >0 :
    prijs = croisanten * 0.39+ stokbroden*2.78- kortingsbonnen*0.5
else: 
    prijs = croisanten * 0.39+ stokbroden*2.78


print(f'De feestlunch kost je bij de bakker {colored(round(prijs, 2), 'yellow',)} euro voor de {colored(croisanten, 'green')} croissantjes en de {colored(stokbroden, 'blue')} stokbroden als de {colored(kortingsbonnen, 'grey')} kortingsbonnen nog geldig zijn!')