import time

PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')
stempel = False
bandje_b = False
bandje_r = False

leeftijd = int(input('Hoe oud ben je? '))
if leeftijd < 18:
    print('Sorry, je mag niet naar binnen')
    time.sleep(2)
    print(f'Probeer het in {18-leeftijd} jaar nog eens.')
    exit()

elif leeftijd >= 18:
    naam = input('Wat is je naam? ').lower()
    if naam not in VIP_LIST:
        if leeftijd >= 21:
            stempel = True
            print('Je krijgt van mij een stempel')
    elif naam in VIP_LIST:
        if leeftijd >= 21:
            bandje_b = True
            print('Je krijgt van mij een blauw bandje')
        elif leeftijd < 21:
            bandje_r = True
            print('Je krijgt van mij een rood bandje')

    drank = input('Wat wil je drinken? ').lower()
    if drank == DRANKJES[0]:
        if bandje_b or bandje_r:
            print("Alstublieft, complimenten van het huis.")
        else:
            print(f'Alsjeblieft je {drank}. Dat is dan {PRIJS_COLA} euro.')
        exit()

    elif drank == DRANKJES[1]:
        if stempel or bandje_b or bandje_r:
            if bandje_b or bandje_r:
                print("Alstublieft, complimenten van het huis.")
            else:
                print(f'Alsjeblieft je {drank}. Dat is dan {PRIJS_BIER} euro.')
        else:
            print('Sorry, je mag geen alcohol bestellen onder de 21.')
            print(f'Probeer het in {21 - leeftijd} jaar nog eens.')
        exit()

    elif drank == DRANKJES[2]:
        if not bandje_b:
            print('Sorry, alleen VIPs mogen champagne bestellen.')
        else:
            print(f'Alsjeblieft je {DRANKJES[2]}. Dat is dan {PRIJS_CHAMPAGNE} euro.')
        exit()

    else:
        print('Sorry, geen idee wat je bedoelt. Hier een glaasje water.')
        exit()
