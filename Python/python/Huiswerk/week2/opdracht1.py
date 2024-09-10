print('-------------------------------------------------')
print(f'10   uitmuntend \n9    zeer goed\n8    goed\n7    ruim voldoende\n6    voldoende\n5    bijna voldoende\n4    onvoldoend\n3    gering\n2    slecht\n1    zeer slecht')
print('-------------------------------------------------')
pers_cijfer = int(input('Voer in jouw cijfer: '))
if pers_cijfer == 10: omschrijving = ('uitmunted!')
elif pers_cijfer == 9: omschrijving= ('zeer goed!')
elif pers_cijfer == 8: omschrijving= ('goed!')
elif pers_cijfer == 7: omschrijving= ('ruim voldoende!')
elif pers_cijfer == 6: omschrijving= ('voldoende!')
elif pers_cijfer == 5: omschrijving= ('bijna voldoende!')
elif pers_cijfer == 4: omschrijving= ('onvoldoende!')
elif pers_cijfer == 3: omschrijving= ('gering!')
elif pers_cijfer == 2: omschrijving= ('slecht!')
elif pers_cijfer == 1: omschrijving= ('zeer slecht!')


if pers_cijfer > 6:
    print(f'Gefeliciteerd, {omschrijving} je resultaat is een {pers_cijfer}')
else:
    print(f'Jammer, {omschrijving} je resultaat is een {pers_cijfer}')