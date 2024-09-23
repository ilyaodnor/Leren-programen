import time, math,random


player_attack = 1
player_defense = 0
player_health = 3

# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
time.sleep(1)
print('Het ruikt hier muf en vochtig.')
time.sleep(1)
print('Je ziet een deur voor je.')
time.sleep(1)
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

antwoord = int(input('Wat toest je in?'))

if antwoord == operation:
    sleutel = True
    print('Het stadbeeld laat de sleutel vallen en je pakt het op')
else:
    sleutel = False
    print('Er gebeurt niets....')

print('Je zie een deur achter het standbeeld.')
print('')
time.sleep(4)

# === [kamer 3] === #
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

# === [kamer 4] === #
zombie_attack = 1
zombie_defense = 0
zombie_health = 2
print(f'Dapper met je nieuwe {baf} loop je de kamer binnen.')
time.sleep(1)
print('Je loopt tegen een zombie aan.')

zombie_hit_damage = (zombie_attack - player_defense)
if zombie_hit_damage <= 0:
    print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
else:
    zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
    
    player_hit_damage = (player_attack - zombie_defense)
    player_attack_amount = math.ceil(zombie_health / player_hit_damage)

    if player_attack_amount < zombie_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de zombie.')
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de zombie te sterk voor je.')
        print('Game over.')
        exit()
print('')
time.sleep(1)

# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')
if sleutel ==True:
    print("Kist met goud is geopend. je heb gewonnen!!")
    exit( )
elif sleutel == False:
    print('Helaas je heb geen sleutel')
    print('Game over')
    exit()