from random import randint
score = 20
te_raden = randint(1, 5)  

while True:
    try:
        gok = int(input('Kies een getal van 1 t/m 5: '))  

        if gok == te_raden:
            print(f'You won! Het juiste getal was {te_raden}. score : {score}')
            break  
        else:
            print('Try again') 
            score -= 1
    except ValueError:
        print('Ongeldige invoer, voer alstublieft een getal in van 1 t/m 5.')


input('Enter')