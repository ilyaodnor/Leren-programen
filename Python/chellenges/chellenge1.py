print('Voor hoeveel mensen wil je yoghurtsalade maken?')

while True:
    personen = input('...')
    if personen.isdigit():
        personen = int(personen)  # Convert the input to an integer
        print(f'-------------------Je hebt nodig voor {personen} personen:-------------------')
        print(f'{personen}             komkommers')
        print(f'{personen} mespunten   fijnzeezout')
        print(f'{personen*2} tenen       knoflook')
        print(f'{personen*15}            verse dille')
        print(f'{personen*500}ml         Griekse yoghurt 10%')
        print(f'{personen} el           wittewijnazijn')
        print(f'{personen*3} el           extra vierge olijfolie')
        print('---------------------------------------------------')
        break
    else:
        print('Voer een cijfer in!')
        continue