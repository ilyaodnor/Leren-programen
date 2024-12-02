boodschappen = {
    'bier': 0,
    'brood': 0 ,
    'hagelslaag': 0 ,
    'melk': 0,
    'beleg': 0,
    'bananen': 0,
    'chips':0
}
keuz = {}
for keys in boodschappen:
    print(keys)

while True:
    artiekel = input('Welk artikel wilt u toevoegen? ').lower()
    hoeveelheid = int(input(f'Hoeveel {artiekel} wilt u toevegen in de lijst? '))
    if artiekel in boodschappen and artiekel not in keuz:
      keuz[artiekel] = hoeveelheid
    elif artiekel in boodschappen and artiekel in keuz:
        keuz[artiekel] = hoeveelheid + keuz[artiekel]
    elif artiekel not in  boodschappen and artiekel not in keuz:
         keuz[artiekel] = hoeveelheid
    elif artiekel not in boodschappen and artiekel in keuz:
        keuz[artiekel] = hoeveelheid + keuz[artiekel]
    while True:
        ja_nee = input('Wilt u nog meer boodchappen toeveogen?').lower()
        if ja_nee == 'ja':
            break
        elif ja_nee == 'nee':
            break
        else:
            print('voeg in ja of nee!! ')
    if ja_nee == 'ja':
        continue
    elif ja_nee == 'nee':
        break
print('----------Boodschappenlijst:----------')
for i in keuz:
    print(i, ':  ', keuz[i])