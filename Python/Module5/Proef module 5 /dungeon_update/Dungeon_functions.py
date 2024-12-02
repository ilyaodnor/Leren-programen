import threading
import math, time, random, os , platform,sys, colorama
def input_check(text, type, expected: list = None): 
    while True:
        if type == int:
            try:
                getal = int(input(text))
                return getal
            except ValueError:
                print("Voer in een integer!")
        elif type == str:
            string = input(f"{text} ").lower()
            if expected: 
                if string in expected:
                    return string
                else:
                    print(f"Voer in een van de volgende opties: {expected}")
            else:
                return string
        elif type == bool:
            try:
                waarde = input(text).strip().lower()
                if waarde in ['true', '1', 'yes', 'y', 'ja']:
                    return True
                elif waarde in ['false', '0', 'no', 'n', 'nee']: 
                    return False
                else:
                    print("Voer 'true' of 'false' in!")
            except ValueError:
                print("Voer een geldige waarde in!")
        else:
            print("Ongeldig type opgegeven!")


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
