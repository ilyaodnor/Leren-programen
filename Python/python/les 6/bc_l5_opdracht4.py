from random import randint

te_raden = randint(1,5)
gok = int(input('Kies een getal van 1 t/m 5: '))

if (te_raden == gok):
    print("Je hebt het getal goed geraden!")
else:
    print("Je hebt het getal niet goed geraden!")