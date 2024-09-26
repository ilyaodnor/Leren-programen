print('Voor hoeveel mensen wil je yoghurtsalade maken?')
while True:
    personen = input('...')
    if personen.isdigit():
        personen = int(personen)  
        print(f'-------------------Je hebt nodig voor {personen} personen:-------------------')
        print(f'{personen/4}             komkommers')
        print(f'{personen/4} mespunten   fijnzeezout')
        print(f'{personen/4} tenen       knoflook')
        print(f'{personen/4*15}            verse dille')
        print(f'{personen/4*500}ml         Griekse yoghurt 10%')
        print(f'{personen/4} el           wittewijnazijn')
        print(f'{personen/4*3} el           extra vierge olijfolie')
        print('---------------------------------------------------')
        break
    else:
        print('Voer een cijfer in!')
        continue