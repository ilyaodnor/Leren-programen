import time, math,random
from functions import gevecht, goblin_shop

player_attack = 1
player_defense = 0
player_health = 3
sleutel = False
rupee = 0 


# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
time.sleep(2)
print('Het ruikt hier muf en vochtig.')
time.sleep(2)
print('Je ziet een deur voor je.')
time.sleep(2)
print('')
time.sleep(3)


#kamer7, 7 --> 3 or 2

kamer_rupee = random.randint(1,11)
if kamer_rupee == 6:
    print('in voolgende kamer je zie een rupee. Je pak het wel.')
    rupee+=1
else:
    print('In voolgende kamer je zie niets.')


time.sleep(1)
while True:
    try:
        kamera1_of_2 = int(input('Er zijn twee deuren in deze kamer. Door welke wil je gaan, de eerste of de tweede?(1/2): '))
        if kamera1_of_2 == 1:
            break
        elif kamera1_of_2 == 2:
             break
        else:
            print('Kies het kamer(1/2)')
            continue
    except ValueError:
        print('Kies het kamer')




    # === [kamer 3] === #
if kamera1_of_2 == 1: 
        
    print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
    time.sleep(2)
    print('Het standbeeld heeft rupee vast.')
    time.sleep(2)
    print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
    time.sleep(2)

    #kamer 2, kamer 2 --> 3 or 6
    getaal = random.randint(10,25)
    getaal2 = random.randint(-5, 75)
    operators = ['+','-','*']
    random_operator = random.choice(operators)
    
    if random_operator == '+':
        operation = getaal + getaal2
    elif random_operator == '-':
        operation = getaal - getaal2
    elif random_operator == '*':
        operation = getaal * getaal2
    
    print(f'Daarboven zie je een som staan {getaal}{random_operator}{getaal2}')

    try: 
        antwoord = int(input('Wat toest je in?'))
    except ValueError:
        antwoord = None

    if antwoord == operation:
        rupee +=1
        print('Het standbeeld laat de rupee vallen en je pakt het op')
    else:
        print('Er gebeurt niets....')
    
        while True:
            try:
                kamera1_of_2 = int(input('Er zijn twee deuren in deze kamer. Door welke wil je gaan, de eerste of de tweede?(1/2): '))
                if kamera1_of_2 == 1:
                    break
                elif kamera1_of_2 == 2:
                    break
                else:
                    print('Kies het kamer(1/2)')
                    continue
            except ValueError:
                print('Kies het kamer')




    if kamera1_of_2 == 1:
        zombie_attack = 1
        zombie_defense = 0
        zombie_health = 2

        player_health = gevecht(player_health, player_defense,player_attack,'Zombie',zombie_attack,zombie_defense,zombie_health)
        if player_health >=0:
            print('Je loopt naar volgende kamer.')
            pass
        elif player_health<0:
            print('helaaszombie was te sterk voor je')
            print('Game over.')
            exit()
        print(f'Je Hp is nu {player_health}')
        time.sleep(2)
        print(f'In deze kamer verkoopt de goblin een schild, een zwaard en een sleutel voor 1 rupee elk.')
        time.sleep(1)


    while True:
            try:
                kamera1_of_2 = int(input('Er zijn twee deuren in deze kamer. Door welke wil je gaan, de eerste of de tweede?(1/2): '))
                if kamera1_of_2 == 1 or kamera1_of_2 == 2:
                    break
                else:
                    print('Kies het kamer')
                    continue
            except ValueError:
                print('Kies het kamer')
    if kamera1_of_2 == 1:

            #Goblinshop
            rupee, player_defense, player_attack, sleutel = goblin_shop(rupee, player_defense, player_attack, sleutel)
            time.sleep(2)
            print('Je loopt naar volgende kamer.')
            time.sleep(2)
            zombie2_attack = 2
            zombie2_defense = 0
            zombie2_health = 3
            time.sleep(1)
            zombie2_hit_damage = (zombie2_attack - player_defense)
            player_hit_damage = (player_attack - zombie2_defense)
            attack_counter2 = 0
            print('Je loopt tegen een rover aan.')
            time.sleep(2)
            print('Hou je vast!')
            time.sleep(2)

            #Final gevecht
            gevecht(player_health, player_defense,player_attack,'Rover',2,0,3)
            if player_health<0:
                    print('Vaiand was te sterk voor je.')
                    print('game over')
                    exit()


                # === [kamer 5] === #
            print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
            print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
            print('Je loopt er naartoe.')
            if sleutel == True:
                    print("Kist met goud is geopend. je heb gewonnen!!")
                    exit( )
            elif sleutel == False:
                    print('Helaas je heb geen sleutel')
                    print('Game over')
                    exit()

elif kamera1_of_2 ==2:
    print("je loopt naar volgende kamer. ")
    pass
        



time.sleep(1)

print('')
time.sleep(1)
# === [kamer 3] === #

print('Je duwt hem open en stap een hele lange kamer binnen.')
time.sleep(2)

time.sleep(2)

game = input('In volgende kamer je zie een gokmachine. Wil je dit gebruiken?(ja of nee)')
if game == 'ja':
    print('''Regels:     
                        Op de tafel zie je twee zeszijdige dobbelstenen
                        Als het totaal punten = vanaf 7 tot 12, krijg je een rupee
                        Als het totaal punten = vanaf 1 tot 6, krijg je -1 HP 
                        Als het totaal punten = 7, krijg je +1 HP en 1 rupee.''')
    while True:
        try:
            start = input(' wil je beginen?')
            if start == 'ja':
                a = random.randint(1,6)
                b = random.randint(1,6)
                print(f'Je krijgt {a} en {b}, samen {a+b}')

                if a + b == 7:
                    print('Jackpot')
                    rupee+=1
                    player_health+=1
                    print(f'*je heb nu {rupee} rupees en {player_health} HP*')
                    time.sleep(3)
                elif a+b in range(8,13):
                    print('je krijgt +1 rupee')
                    rupee+=1
                    print(f'Je hebt nu {rupee} rupees')
                   
                    time.sleep(3)
                elif a+b in range(1,7):
                    player_health-=1
                    print('Helaas je hebt verloren')
                    print(f'Je hebt nu {player_health}HP')
                    if player_health == 0:
                        print('game over ')
                        exit()


            elif start == 'nee':
                break
            
        except ValueError:
            print('Voer in ja of nee')
else:
    pass





while True:
    try:
        kamera1_of_2 = int(input('Er zijn twee deuren in deze kamer. Door welke wil je gaan, de eerste of de tweede?(1/2): '))
        if kamera1_of_2 == 1:
                    break
        elif kamera1_of_2 == 2:
                    break
        else:
                    print('Kies het kamer(1/2)')
                    continue    
    except ValueError:
        print('Voer in 1 of 2.')
if kamera1_of_2 == 1:
    print('In deze kamer je ziet een goblin welke verkogt iets.')

    rupee, player_defense, player_attack, sleutel = goblin_shop(rupee, player_defense, player_attack, sleutel)
    time.sleep(2)
    print('Je loopt naar volgende kamer. ')

    print('Je loopt tegen een rover aan.')
    time.sleep(2)
    print('Hou je vast!')
    time.sleep(2)



        #final gevecht
    gevecht(player_health, player_defense,player_attack,'Rover',2,0,3)
    if player_health<=0:
                    print('Vaiand was te sterk voor je.')
                    print('game over')
                    exit()


                    # === [kamer 5] === #
    print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
    print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
    print('Je loopt er naartoe.')
    if sleutel == True:
         print("Kist met goud is geopend. je heb gewonnen!!")
         exit( )
    elif sleutel == False:
                        print('Helaas je heb geen sleutel')
                        print('Game over')
                        exit()









time.sleep(1)
print(' je ga naar volgende kamer.')
buf = random.randint(1,2)
time.sleep(2)
if buf == 1:
    player_defense+=1
    print(f'In deze kamer vond je een verdedigingsdrankje.Je krijg +1 defensie. Nu je hebt {player_defense}Def. ')
    time.sleep(1)
    print('Je loopt verder naar volgende kamer. ')
    time.sleep(1)
elif buf == 2:
    player_health+=2
    print(f'In deze kamer vond je een gezondheidsdrankje.Je krijg +2 HP.Nu je hebt {player_health}HP')
    time.sleep(1)
    print('Je loopt verder naar volgende kamer. ')
    time.sleep(1)

time.sleep(3)

print(f'In deze kamer verkoopt de goblin een schild, een zwaard en een sleutel voor 1 rupee elk.')
time.sleep(1)
om_te_kopen = [1, 2, 3]  # 1: Schild, 2: Zwaard, 3: Sleutel

rupee, player_defense, player_attack, sleutel = goblin_shop(rupee, player_defense, player_attack, sleutel)


time.sleep(2)



zombie2_attack = 2
zombie2_defense = 0
zombie2_health = 3

time.sleep(1)

zombie2_hit_damage = (zombie2_attack - player_defense)
player_hit_damage = (player_attack - zombie2_defense)
attack_counter2 = 0

print('Je loopt tegen een rover aan.')
time.sleep(2)
print('Hou je vast!')
time.sleep(2)
player_health = gevecht(player_health, player_defense,player_attack,'Rover',2,0,3)
if player_health<0:
    print('Vaiand was te sterk voor je.')
    print('game over')
    exit()
print(player_health)


# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')
if sleutel == True:
    print("Kist met goud is geopend. je heb gewonnen!!")
    exit( )
elif sleutel == False:
    print('Helaas je heb geen sleutel')
    print('Game over')
    exit()