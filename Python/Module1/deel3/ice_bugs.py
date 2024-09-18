
SMALL_PRICE = 1.25
MEDIUM_PRICE = 2.10

amount = int(input(f'Hoeveel ijsjes van 1,25 wil je bestellen? '))
amount2 = int(input(f'En hoeveel ijsjes van 2,10 wil je bestellen? '))
totalPrice = float(amount * SMALL_PRICE) + float(amount2 * MEDIUM_PRICE)
getal = str(totalPrice).replace('.',',')
print(f'Dat is dan {getal} totaal')