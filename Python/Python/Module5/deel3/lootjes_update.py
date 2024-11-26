import random
import os
import time

namen = {}  
cadeus = {}
while True:
    name = input('Voer in een naam: ').lower()

    if name not in namen:
        namen[name] = name  
        cadeus[name] = input('Voer de drie geschenken in, gescheiden door komma\'s ')
        if len(namen) >= 3:  
            ja_nee = input('Wilt u nog een naam invoeren? (ja/nee) ').lower()
            if ja_nee == 'nee':
                break  
    else:
        print('Voer een nieuwe naam in!!')

namen_kopie = list(namen.keys()) 
wie_is_wie = {}

for name in namen:
    random_name = random.choice(namen_kopie)
    
    while random_name == name:  
        random_name = random.choice(namen_kopie)

    wie_is_wie[name] = random_name
    namen_kopie.remove(random_name)  

pogingen = 0
while pogingen != len(namen): 
    os.system('clear')
    
    a =input('Voer in je naam: ')
    if a in wie_is_wie:
        value = wie_is_wie[a]
        print(f'{a} krijgt {value}, jij moet kopen {cadeus[value]} voor hem.')
        pogingen+=1

    input('Druk op enter om door te gaan : ')
input('enter')
print(f'Kopie namen: \n{wie_is_wie}')
print(cadeus)