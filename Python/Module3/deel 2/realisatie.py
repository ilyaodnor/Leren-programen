import random
random_getal = random.randint(1,1001)

rondjes=0
gewonen = False
poging = True
while poging:
    score = 0
    for i in range(20):
        rondjes+=1
        getal = int(input('Voer in het getal: '))
        gewonen = True
        if getal == random_getal:
            break
        elif getal>random_getal:
            print('Jouw getsal is hooger.')
        elif getal<random_getal:
            print('Jouw getsal is lager')
        if abs(getal-random_getal)<20:
            print('Je bent heel warm.')
        elif 20<abs(getal-random_getal)<50:
            print('Je bent warm. ')
    if gewonen:
        score+=1
        print(f'Je hebt gewonen met {rondjes} rondjes, jouw scoren zijn: {score}')
    nog_een_keer=input('Wilt u nog een keer spelen?').lower()
    if nog_een_keer == 'ja':
        continue
    elif nog_een_keer == 'nee':
        break
print(f'Jouw score is {score}')



    