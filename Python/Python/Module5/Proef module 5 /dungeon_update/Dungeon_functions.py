import math, time, random, os , platform,sys, colorama
def input_check(text, type,expected: list): # Input checken

    while True:
        if type == int:
            try:
                getal = int(input_slow(text, delay=0.2))
                return getal
            except ValueError:
                print('Voer in een integer! ')
        elif type == str:
            string = str(input_slow(f'{text} '))
            if string in expected:     
                return string
            else:
                print(f'voer in ({expected})')
        elif type == bool:
            try:
                getal = bool(input_slow(text))
                return getal
            except ValueError:
                print('Voer in een getal!')



def print_slow(text, delay=0.05,): 
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def input_slow(prompt, delay=0.05):
    print_slow(prompt, delay)
    return input()

def fight(player: dict, enemy: dict):   #fight
    print(f"{colorama.Fore.RED}Je vecht tegen {enemy['name']}!{colorama.Style.RESET_ALL}")
    while player["hp"] > 0 and enemy["hp"] > 0:
        enemy["hp"] -= max(0, player["attack"] - enemy["defense"])
        if enemy["hp"] <= 0:
            print(f"Je hebt {enemy['name']} verslagen!")
            print_slow(f'Je hebt nu {player['hp']} HP')
            return True

        player["hp"] -= max(0, enemy["attack"] - player["defense"])
        if player["hp"] <= 0:
            print("Je bent verslagen...")
            return False
        


def kies_kamer():
    print_slow('Je ziet in deze kamer twee duren')
    antwoord = input_check('Voer in kamer 1 of kamer 2', str, ['1','2'])
    if antwoord == '1':
        print_slow('je loopt verder')
        return True
    elif antwoord == '2':
        print_slow('Je loopt verder.')
        return False

def clear_screen():
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
