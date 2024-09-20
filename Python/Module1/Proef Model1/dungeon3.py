import time, math,random


player_attack = 1
player_defense = 0
player_health = 3

# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
time.sleep(2)
print('Het ruikt hier muf en vochtig.')
time.sleep(2)
print('Je ziet een deur voor je.')
time.sleep(2)
print('')
time.sleep(3)

# === [kamer 2] === #

print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
time.sleep(2)
print('Het standbeeld heeft een sleutel vast.')
time.sleep(2)
print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
time.sleep(2)
getaal = random.randint(10,25)
getaal2 = random.randint (-5, 75)
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
    antwoord=None

if antwoord == operation:
    sleutel = True
    print('Het stadbeeld laat de sleutel vallen en je pakt het op')
else:
    sleutel = False
    print('Er gebeurt niets....')

print('Je zie een deur achter het standbeeld.')
print('')
time.sleep(4)
while True:
    try:
        kamera1_of_2 = int(input('Er zijn twee deuren in deze kamer. Door welke wil je gaan, de eerste of de tweede?(1/2): '))
        if kamera1_of_2 == 1 or 2:
            break
        else:
            print('Kies het kamer')
    except ValueError:
        print('Kies het kamer')
    # === [kamer 3] === #
if kamera1_of_2 == 1:
    zombie_attack = 1
    zombie_defense = 0
    zombie_health = 2

    time.sleep(1)
    print('Je loopt tegen een zombie aan.')
    player_hit_damage = (player_attack - zombie_defense)
    zombie_hit_damage = (zombie_attack - player_defense)
    attack_counter = 0
    while True:
        zombie_health = zombie_health-(player_attack - zombie_defense)
        print('De zombie raakt jou.')
        time.sleep(1)
        player_health = player_health-(zombie_attack-player_defense)
        print("Je raakt de zombie.")    
        time.sleep(1)
        attack_counter+=1
        if player_health>0 and zombie_health <= 0:
            print(f'In {attack_counter} rondes versla je de zombie.')
            print('Je ga verder')
            time.sleep(1)
            print(f'Je health is nu  {player_health}')
            break
        elif zombie_health>0 and player_health <= 0:
            print('De zombie is te sterk voor je ')
            time.sleep(1)
            print('Game over ')
            exit()
    print('')
    time.sleep(1)
    # === [kamer 4] === #
    item = ['schild', 'zwaard']
    baf = random.choice(item)
    if baf == 'schild':
        player_defense += 1
    elif baf == 'zwaard':
        player_attack+=2

    print('Je duwt hem open en stap een hele lange kamer binnen.')
    time.sleep(2)
    print(f'In deze kamer staat een tafel met daarop een {baf}.')
    time.sleep(2)
    print(f'Je pakt het {baf} op en houd het bij je.')
    time.sleep(2)
    print('Op naar de volgende deur.')
    time.sleep(2)
    print('')
    time.sleep(3)

elif kamera1_of_2 == 2:
    item = ['schild', 'zwaard']
    baf = random.choice(item)
    if baf == 'schild':
        player_defense += 1
    elif baf == 'zwaard':
        player_attack+=2

    print('Je duwt hem open en stap een hele lange kamer binnen.')
    time.sleep(2)
    print(f'In deze kamer staat een tafel met daarop een {baf}.')
    time.sleep(2)
    print(f'Je pakt het {baf} op en houd het bij je.')
    time.sleep(2)
    print('Op naar de volgende deur.')
    time.sleep(2)
    print('')
    time.sleep(3)

zombie2_attack = 2
zombie2_defense = 0
zombie2_health = 3

time.sleep(1)
print('Je loopt tegen een zombie aan.')

zombie_hit_damage = (zombie2_attack - player_defense)
attack_counter2 = 0

print('Je loopt tegen een zombie aan.')
while True:
    zombie_health2= zombie2_health-(player_attack - zombie2_defense)
    print('De zombie raakt jou.')
    time.sleep(1)
    player_health = player_health-(zombie2_attack-player_defense)
    print("Je raakt de zombie.")   
    time.sleep(1) 
    attack_counter2+=1
    if player_health>0 and zombie2_health == 0:
        print(f'In {attack_counter} rondes versla je de zombie.')
        time.sleep(1)
        print('Je ga verder')
        print(f'Je health is nu  {player_health}')
        break
    elif zombie2_health>0 and player_health == 0:
        print('De zombie is te sterk voor je ')
        time.sleep(1)
        print('Game over ')
        
        exit()

# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')
if sleutel:
    print("Kist met goud is geopend. je heb gewonnen!!")
    exit( )
elif sleutel:
    print('Helaas je heb geen sleutel')
    print('Game over')
    exit()