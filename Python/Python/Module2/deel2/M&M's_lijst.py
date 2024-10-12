import random


kleuren = ['orange', 'blauw', 'groen','bruin']

toevoegen = int(input('Hoeveel M&M\'s er aan de zak toegevoegd moeten worden?'))
if toevoegen>0:
    inhoud = []


    for i in range(4):
        if i == 3:
            amount = toevoegen - sum(inhoud)
    
        else:
            amount = random.randint(0,toevoegen - sum(inhoud) - (3-i))
        inhoud.append(amount)
        
    zak = []
    for kleur, aantal in zip(kleuren, inhoud):
        zak.append(f'{kleur}: {aantal}')
    print(zak)

elif toevoegen == 0:
    
    zak = [f'{kleur}: 0' for kleur in kleuren]


    print(zak)
else:
    print('dat kan niet.')
    