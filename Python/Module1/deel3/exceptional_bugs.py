import random

#selecteer 2 nummers
num1 = int(random.randint(1,10))
num2 = int(random.randint(5,15))

#vraag om een antwoord


#geef reactie op het antwoord
while True:
        number = int(input(f'Weet jij wat {num1} + {num2}  is? ') )

        if int(number == num1+num2):
            print('Dat is juist')
            break

        elif int(number != num1+num2):
            print('Nee dat klopt niet')
        else:
            print('Dat is geen nummer!')
