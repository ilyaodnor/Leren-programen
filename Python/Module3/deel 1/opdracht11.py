from fruitmand import fruitmand
kleuren = []
for i in fruitmand:
    if i['color'] not in kleuren:
        kleuren.append(i['color'])
print(kleuren[2:],': ')
while True:
    keuz = str(input(f'Voer in het kleur: \n{kleuren}'))
    if keuz in kleuren:
        break
    else:
        print(f'De kleur {keuz} zit er niet in de fruitmand')
ronde_vruchten =0
niet_ronde = 0
for fruit in fruitmand:
    if fruit['color'] == keuz:
        if fruit['round'] == True:
            ronde_vruchten+=1
        else:
            niet_ronde+=1

if ronde_vruchten>niet_ronde:
    verschiel = ronde_vruchten - niet_ronde
    print(f'Vergschiel tussen ronde en niet ronde is {verschiel}')
elif ronde_vruchten<niet_ronde:
    verschiel = niet_ronde - ronde_vruchten
    print(f'Vergschiel tussen niet ronde en ronde is {verschiel}')
else:
    print('Ze zijn gelijk.')

