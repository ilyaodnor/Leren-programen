from dungeon_data import rooms, enemies, player_data, items_for_sale
from Dungeon_functions import print_slow, input_slow, fight, kies_kamer, clear_screen, input_check
import random, time

# === [kamer 0] === #
def kamer_0():
    clear_screen()
    print_slow('''Door de twee grote deuren loop je een gang binnen.
Het ruikt hier muf en vochtig.
Je ziet een deur voor je.''')
    clear_screen()
    kamer_1()

# === [kamer 1] === #
def kamer_1():
    random_getal = random.randint(1, 10)
    if random_getal == 5:
        print_slow('Je hebt een rubin gevonden!')
    else:
        print_slow('In deze kamer zie je niets.')
    een_of_twee = kies_kamer()
    if een_of_twee:
        clear_screen()
        kamer_8()
    else:
        clear_screen()
        kamer_7()

# === [kamer 7] === #
def kamer_7():
    print_slow(rooms[2])
    print_slow("Een standbeeld staat voor je.")
  
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    opper = random.choice(['-', '+'])

    if opper == '+':
        correct = num1 + num2
    else:
        correct = num1 - num2

    answer = int(input_check(f"Los de som op: {num1} {opper} {num2} = ", int))
    
    if answer == correct:
        print_slow("Correct! Je hebt een rubin gekregen.")
        player_data["rubins"] += 1
    else:
        print_slow("Fout! Het standbeeld blijft gesloten.")
    
    een_of_twee = kies_kamer()
    if een_of_twee:
        clear_screen()
        kamer_6()
    else:
        clear_screen()
        kamer_8()

# === [kamer 6] === #
def kamer_6():
    print_slow('Voorzichtig open je de deur, je wilt geen zombie tegenkomen.') 
    print_slow('Tot je verbazing zie je iets in het midden van de kamer staan.')
    print_slow('Je loopt er naartoe.')
   
    print_slow(f'Je loopt de kamer binnen.')
    print_slow(f'Je komt een {enemies[0]["name"]} tegen.')
    gevecht = fight(player_data, enemies[0])
    if not gevecht:
        print_slow('Game over.')
        exit()

    een_of_twee = kies_kamer() 
    if een_of_twee:
        clear_screen()
        kamer_3()
    else:
        clear_screen()
        kamer_8()
    print_slow('Je gaat verder.')

# === [kamer 8] === #
def kamer_8():
    print_slow(f'Hier zie je {rooms[3]}. Regels:\n'
               '- Als de dobbelstenen 7 zijn: +1 Rubin en +1 HP.\n'
               '- Als de dobbelstenen meer dan 7 zijn: +1 Rubin.\n'
               '- Als de dobbelstenen minder dan 7 zijn: -1 HP.')
    while True:
        antwoord = input_check("Wil je in het casino spelen? (Ja/Nee): ", str, ['ja','nee'])
        if antwoord == 'ja':
            roll = random.randint(1, 6) + random.randint(1, 6)
            print_slow(f"De goblin gooit dobbelstenen: {roll}")
            if roll == 7:
                print_slow('Je krijgt 1 rubin en 1 HP.')
                player_data['hp'] += 1
                player_data['rubins'] += 1
            elif roll > 7:
                print_slow("Je wint 1 rubin!")
                player_data["rubins"] += 1
            else:
                print_slow("Je verliest 1 HP!")
                player_data["hp"] -= 1
                if player_data['hp'] == 0:
                    clear_screen()
                    print_slow('Je hebt nu 0 HP')
                    print_slow('Game over')
                    exit()
        else: 
            break
    een_of_twee = kies_kamer()
    if een_of_twee:
        clear_screen()
        kamer_9()
    else:
        clear_screen()
        kamer_3()

# === [kamer 9] === #
def kamer_9():

    buff = random.randint(1, 2)
    if buff == 1:
        player_data['hp'] += 2
        print_slow(' In deze kamer zie je een potion.')
        print_slow('*Je drinkt het*')
        print_slow('Je hebt +2 HP gekregen.')
    elif buff == 2:
        print_slow(' In deze kamer zie je een potion.')
        print_slow('*je drinkt het*')
        player_data['attack'] += 1

        print_slow('Je hebt +1 attack gekregen.')
    time.sleep(2)
    clear_screen()
    kamer_3()

# === [kamer 3] === #
def kamer_3():
    print_slow('In deze kamer zie je een goblin-verkoper.')

    while player_data['rubins'] > 0 and items_for_sale:
        print_slow(f"Beschikbare items te koop: {', '.join(items_for_sale.keys())}")
        print_slow(f"Je hebt {player_data['rubins']} rubin(en).")
        
        item = input_slow("Kies een item: ").strip().lower() 
        if item in items_for_sale:
            stat, cost = items_for_sale[item]
            if player_data['rubins'] >= cost:
               
                if item == 'sleutel':
                    player_data['sleutel'] = True
                else:
                    player_data[stat] += cost
                player_data['rubins'] -= cost
                items_for_sale.pop(item)
                print_slow(f"Je hebt {item} gekocht! Je hebt nu {player_data['rubins']} rubin(en) over.")
            else:
                print_slow("Niet genoeg rubins!")
        else:
            print_slow(f"Onjuist item. Kies uit: {', '.join(items_for_sale.keys())}")

    print_slow("Geen rubins meer of niets meer te koop.")
    print(player_data)
    time.sleep(5)
    clear_screen()
    kamer_4()
# === [kamer 4] === #
def kamer_4():
    print_slow(rooms[4])
    if fight(player_data, enemies[1]):
        clear_screen()
        kamer_5()
    else:
        clear_screen()
        print_slow("Je hebt verloren!")
        exit()

# === [kamer 5] === #
def kamer_5():
    print_slow(rooms[5])
    if player_data['sleutel']:
        print_slow("Je opent de kist en wint het spel!")
    else:
        print_slow("Je hebt geen sleutel om de kist te openen. Het spel is voorbij.")
    exit()

# === [Start van het spel] === #
def start_game():
    print_slow("Welkom in de dungeon!")
    kamer_0()
