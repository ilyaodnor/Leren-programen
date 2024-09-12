while True:
    try:
        vraag = int(input('Is de kaas geel? (1 voor ja, 2 voor nee): ').strip())
        if vraag == 1:
            vraag = int(input('Zitten er gaten in de kaas? (1 voor ja, 2 voor nee): ').strip())
            if vraag == 1:
                vraag = int(input('Is de prijs van de kaas hoog? (1 voor ja, 2 voor nee): ').strip())
                if vraag == 1:
                    print('Emmenthaler')
                else:
                    print('Leerdammer')
            else:
                vraag = int(input('Is de kaas erg hard? (1 voor ja, 2 voor nee): ').strip())
                if vraag == 1:
                    print('Parmigiano Reggiano')
                else:
                    print('Goudse kaas')
        elif vraag == 2:
            vraag = int(input('Heeft de kaas blauwe schimmel? (1 voor ja, 2 voor nee): ').strip())
            if vraag == 1:
                vraag = int(input('Heeft de kaas een korst? (1 voor ja, 2 voor nee): ').strip())
                if vraag == 1:
                    print('Blue de Rochbaron')
                else:
                    print("Foume d'Ambert")
            else:
                vraag = int(input('Heeft de kaas een korst? (1 voor ja, 2 voor nee): ').strip())
                if vraag == 1:
                    print('Camembert')
                else:
                    print('Mozzarella')
        else:
            print('Voer alleen 1 of 2 in als antwoord!')
            continue
        break
    except ValueError:
        print('Voer een getal in, 1 of 2!')
