import time, math
import random
from funcdungeon import fight

player_attack = 2
player_defense = 0
player_health = 3
sleutel = False
rubin=0
skip_kamer2=False
skip_kamer6=False
skip_kamer8=False
skip_kamer9=False

# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.') 
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(2)
# === [kamer 7] === #
wizard = random.randint(1, 10)
if wizard == 1 :
    print('')
else :
    rubin +=1
    print('Je ziet rubin op de grond liggen')
    print('je pakt rubbin')
   
time.sleep(2)

while True:
        cameras2 = input('je moet kamer gaan kiezen gaa je naar kamer 1 of naar kamer 2?')
        print('Je komt niet meer terug ')
        cameras='1'
        cameras3='2'
        if cameras2 == cameras :
            print ('je gaat naar volgende kamer ')
            skip_kamer2 = True
            break
        elif cameras2 == cameras3:
            skip_kamer2 = False
            print ('je gaat naar volgende kamer ; ')
            break
        else:
            print('Kies 1 of 2')
time.sleep(2)

# === [kamer 2] === #
if skip_kamer2 == True:
    print('Je hebt een kamer gemist maar je gaat verder')
elif skip_kamer2 == False:
    print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
    num1 = random.randint(10, 25) 
    num2 = random.randint(-5, 75) 
    operation = random.choice(['+', '-'])
    print('Het standbeeld heeft een rubin vast.')
    print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
    print('Daarboven zie je een som staan')
    if operation == '+':
            goedantwoord = num1 + num2
            print(f'De som is: {num1} + {num2}')
            antwoord = input('Wat toets jij in ')
    else:
            goedantwoord = num1 - num2
            print(f'De som is: {num1} - {num2}')
            antwoord = input('Wat toets jij in ')
    if  goedantwoord and int(goedantwoord) == goedantwoord:
            rubin += 1  
            print('Je hebt de rubin  gekregen')
    else:
            print('Er gebeurt niets')

            
while True:
        cameras2 = input('je moet kamer gaan kiezen gaa je naar kamer 1 of naar kamer 2?')
        print('Je komt niet meer terug ')
        if cameras2 == '1' :
            print ('je gaat naar volgende kamer ')
            skip_kamer6 = True
            break
        elif cameras2 == '2':
            skip_kamer6 = False
            print ('je gaat naar volgende kamer ; ')
            break
        else:
            print('Kies 1 of 2')    
            

print('Je zie een deur achter het standbeeld.')
print('')

time.sleep(2)

if skip_kamer6 == True:
    print('Je gaat verder') 
elif skip_kamer6 == False:
# === [kamer 6] === #
    print('Voorzichtig open je de deur, je wilt niet een zombie tegenkomen.') 
    print('Tot je verbazig zie je een  in het midden van de kamer staan.')
    print('Je loopt er naartoe.')
    zombie_attack = 1
    zombie_defense = 0
    zombie_health = 2
    zombie_name='Dohlyak'
    print(f' loop je de kamer binnen.')
    print(f'Je loopt tegen een {zombie_name} aan.')
    fight(player_attack, player_defense, player_health, zombie_attack, zombie_defense, zombie_health,zombie_name)

    while True:
            cameras2 = input('je moet kamer gaan kiezen gaa je naar kamer 1 of naar kamer 2?')
            print('Je komt niet meer terug ')
            cameras='1'
            cameras3='2'
            if cameras2 == cameras :
                print ('je gaat naar volgende kamer ')
                skip_kamer8 = True
                break
            elif cameras2 == cameras3:
                skip_kamer8 = False
                print ('je gaat naar  volgende kamer ; ')
                break
            else:
                print('Kies 1 of 2')    

                print('')

            time.sleep(2)

if skip_kamer8 == True :
    print('Je gaat verder')
# === [kamer 3] === #
elif skip_kamer8 == False:
    while True:
        казик = input('Goblin vraagt of je in het casino wilt spelen. Jij kan alleen Ja of Nee zeggen: ')
        total=0
        if казик == 'Ja':
            dobbelstenen = random.randint(1, 6)  
            dobbelstenen2 = random.randint(1, 6)  

            print(f'De goblin gooit de dobbelstenen op tafel. Op de eerste dobbelsteen: {dobbelstenen}, op de tweede dobbelsteen: {dobbelstenen2}')
            total = dobbelstenen + dobbelstenen2
            if total >=7:
                rubin += 1
                print('Je kright +1 rubin')
            elif total == 7:
                player_health += 4
                print('Je kright 4 Health')
            else:
                player_health -= 1
                print('-1HP')

                if   player_health == 0:
                    exit('Je hebt verlist')

        elif казик == 'Nee':
            print('Je gaat verder en wilt niet in het casino spelen.')
            break 

        else:
            print('Je kunt alleen Ja of Nee zeggen.')
if skip_kamer6 == True:
    print ('deze kamer is dicht')
    while True:
        cameras2 = input('je moet kamer gaan kiezen gaa je naar kamer 1 of naar kamer 2?')
        print('Je komt niet meer terug ')
        cameras='1'
        cameras3='2'
        if cameras2 == cameras :
            print ('je gaat naar volgende kamer ')
            skip_kamer9 = True
            break
        elif cameras2 == cameras3:
            skip_kamer9 = False
            print ('je gaat naar volgende kamer ; ')
            break
        else:
            print('Kies 1 of 2')    
            
# === [kamer 6] === #

skip_kamer9 == False
print('Er geburt niet')

if not skip_kamer9:
    buff = random.randint(1, 2)
    if buff == 1:
        player_health += 2
    elif buff == 2:
        player_attack += 1
        print('Je Voelt iets')
    
else:
    print('Je gaat verder')
time.sleep(2)
  

items_for_sale = ['Schild', 'Attack','Sleutel']

print('Je ziet een goblin die iets verkoopt, je loopt naar de goblin.')
print('Hij verkoopt een Schild en Attack buff, beide kosten 1 rubin.')

while rubin > 0 and items_for_sale:
    print(f"Beschikbare items te koop: {', '.join(items_for_sale)}")
    print(f"Je hebt {rubin} rubin(en).")

    item = input('Kies een van deze: Schild(1) of Attack(1) buff of Sleutel(2) : ')

    if item == 'Schild' and 'Schild' in items_for_sale:
        player_defense += 1
        items_for_sale.remove('Schild')
        rubin -= 1
        print('Je hebt een Schild gekocht, je defense is nu verhoogd!')
        print(f"Nu heb je {rubin} rubin(en) over.")
    
    elif item == 'Attack' and 'Attack' in items_for_sale:
        player_attack += 1
        items_for_sale.remove('Attack') 
        rubin -= 1 
        print('Je hebt een Attack buff gekocht, je aanval is nu verhoogd!')
        print(f"Nu heb je {rubin} rubin(en) over.")

    elif item  == 'Sleutel' and 'Sleutel' in items_for_sale:
        sleutel = True
        items_for_sale.remove('Sleutel')
        rubin -= 2
        print('Je hebt Sleutel gekocht')
    
    else:
        print(f'Jij kan alleen een {items_for_sale}.')
    
    if not items_for_sale:
        print('Er zijn geen items meer te koop.')
        break
    elif rubin == 0:
        print('Je hebt geen rubins meer.')
        break

print('Je hebt alle beschikbare aankopen gedaan en gaat verder.')

         
print (f'Items die te koop nog {items_for_sale}')

print(f'Je betalt  1 rubin  for {item}')
print(f'Je pakt het {item} op en houd het bij je.')
print('Op naar de volgende deur.')
print('')
time.sleep(2)
# === [kamer 4] === #
print('Voorzichtig open je de deur, je wilt niet een zombie tegenkomen.') 
print('Tot je verbazig zie je een zombie in het midden van de kamer staan.')
print('Je loopt er naartoe.')
zombie_attack = 2
zombie_defense = 0
zombie_health = 3
zombie_name='Gromilla'

print(f'Dapper met je nieuwe {item} loop je de kamer binnen.')
print(f'Je loopt tegen een {zombie_name} aan.')

fight(player_attack,player_defense,player_health,zombie_attack,zombie_defense,zombie_health,zombie_name)
print('')
time.sleep(3)

# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')
if sleutel == False:
    print (' Jij hebt geen sleutel om kist te openen ')
    exit()
elif sleutel == True :
    print ('Je hebt sleutel dus jij opent  kist en jij hebt gewonen')
    exit()