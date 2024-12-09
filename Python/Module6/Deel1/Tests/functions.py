import time, os, sys
from data import* 
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
                    print('sorry, dat snap ik niet. ')
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



def clear_screen():
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text, delay=0.05,): 
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def input_slow(prompt, delay=0.05):
    print_slow(prompt, delay)
    return input()


def start():    
    try:
            hoeveelheid = input_check("Hoeveel bolletjes wilt u? ", int)
            if 1 <= hoeveelheid <= 3:
                form_type = input_check(
                    f"Wilt u deze {hoeveelheid} bolletje(s) in een hoorntje of een bakje? ", str, SERVER_OPTIES
                )
                if form_type in ["een hoorntje", "hoorn", "een hoorn"]:
                    form_type = "hoorntje"
                elif form_type in ["bak", "bakje", "een bak", "een bakje"]:
                    form_type = "bakje"
                # serve_bolletje(hoeveelheid, form_type)
                return f"Hier is uw {form_type} met {hoeveelheid} bolletje(s)."
            elif 4 <= hoeveelheid <= MAX_BOLLETJES:
                # print(f"Dan krijgt u van mij een bakje met {hoeveelheid} bolletjes.")
                return f"Dan krijgt u van mij een bakje met {hoeveelheid} bolletjes."
            else:
                return "Sorry, zulke grote bakken hebben we niet."

    except ValueError:
            print("Sorry, dat snap ik niet.")