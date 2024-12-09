import functions, colorama, time
from data import *
from functions import *

while True:
    
    clear_screen()
    print('Welkom bij Papi Gelato.')
    time.sleep(1)
    antwoord = input_check('Bent u 1)particuleer of 2)zakelijke klant?', str, ['1','2'])
    if antwoord == '1':
        while True:
            bestelen_particuliere_klant(besteling, smaken_kiez, gekozen_smaken, gekozen_saus)
            antwoord = input_check('Wilt u nog iets bestellen?', bool)
            if antwoord!=True:
                functions.rekening_particuliere_klant(besteling, gekozen_smaken, gekozen_saus)
                break
    else:
        while True:
            bestelen_zakelijke_klant(besteling_zakelijke)
            antwoord = input_check('Wilt u nog iets bestellen?', bool)
            if antwoord!=True:
                functions.rekening_zakijke(besteling_zakelijke)
                break

    print("Bedankt en tot ziens!")
    besteling, besteling_zakelijke, gekozen_saus, gekozen_smaken = reset_orders(
        besteling,besteling_zakelijke, gekozen_smaken, gekozen_saus)
    input('Druk op Enter om door te gaan...')
