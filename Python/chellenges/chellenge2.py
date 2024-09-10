grond = 3*1.5*8
uitgraven_kosten = 25*grond
afvoer_kosten = 32.5 * grond

voorrijkosten = 250 + 2.05*60
vierkante_meters = 24+24+9
beton_kosten = vierkante_meters *200
totaal = uitgraven_kosten + afvoer_kosten + voorrijkosten + beton_kosten

print(f'Offerte voor een zwembad \nvan 8 bij 3 bij 1,5 meter (inhoud: {grond} m3):\n')
print(f'Uitgraven:                    €{uitgraven_kosten}')
print(f'Afvoeren grond:               €{afvoer_kosten}')
print(f'Voorrijkosten                 €{voorrijkosten}')
print(f'Beton + tegel (xx m2)         €{beton_kosten}\n\n')
print(f'                      Totaal: €{totaal}')