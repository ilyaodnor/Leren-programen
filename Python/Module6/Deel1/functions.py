import time, os, sys
from data import* 
def reset_orders(besteling_zakelijke, gekozen_smaken, gekozen_saus, besteling):
    besteling = {'bolletjes': 0, 'hoorentjes': 0, 'bakjes': 0}
    besteling_zakelijke = {}
    gekozen_smaken = {
    'mint':0,
    'vanile':0,
    'chocolade':0,
    'aardbei':0
}
    gekozen_saus = {}
    return besteling, besteling_zakelijke, gekozen_saus, gekozen_smaken



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
                    print(vout_melding)
                    print(f"Voer in een van de volgende opties: {expected}")
            else:
                return string
        elif type == bool:
            try:
                waarde = input(text).strip().lower()
                if waarde in ['true', '1', 'yes', 'y', 'ja', 'j']:
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

def particuliere_klant():
    antwoord = input_check('Bent u 1) een particuliere klant of 2) een zakelijke klant?', str, ['1','2','particuliere klant', 'zakelijke kalnt'])
    if antwoord in ['1','particuliere klant']:
        return True
    else:
        return False

def form_typ(hoeveelheid, besteling):
    form_type = input_check(f"Wilt u deze {hoeveelheid} bolletje(s) in een hoorntje of een bakje? ", str, SERVER_OPTIES)
    if form_type in ["een hoorntje", "hoorn", "een hoorn"]:
        besteling['hoorentjes'] += 1 
        return "hoorntje", 
    elif form_type in ["bak", "bakje", "een bak", "een bakje"]:
        besteling['bakjes'] += 1
        return "bakje"
    


def smaken_kies(hoeveelheid: int, smaken_kiez: list, gekozen_smaken: dict) -> dict:
    for i in range(1, hoeveelheid + 1):  
        smaak = input_check(
            f"Welke smaak wilt u voor bolletje {i}? ({', '.join(smaken_kiez)})", 
            str, 
            smaken_kiez)

        smaak = smaak.lower()

        if smaak in gekozen_smaken:
            gekozen_smaken[smaak] += 1
        else:
            print(f"De smaak '{smaak}' is niet beschikbaar.")
    return gekozen_smaken


def saus(hoeveelheid: int, gekozen_saus: dict, besteling: dict) -> dict:
    antwoord = input_check(
        "Wilt u nog topping bij? (true/false): ", bool)
    if antwoord:
        topping = input_check(
            "Welke topping wilt u? \n- Caramel in bakje (€0.90) \n- Caramel in hoorntje (€0.60) \n- Sprinkels (€0.30 per bolletje)\n- Slagroom (€0.50)\n", 
            str, 
            ['slagroom', 'caramel', 'sprinkels']
        )

        if topping == 'caramel':
            if besteling['hoorentjes'] > 0:
                gekozen_saus['caramel'] = CARAMEL_SAUS_HOORN
            elif besteling['bakjes'] > 0:
                gekozen_saus['caramel'] = CARAMEL_SAUS_BAKJE
            else:
                print("Caramel kan alleen toegevoegd worden aan een hoorntje of een bakje.")
        
        elif topping == 'sprinkels':
            gekozen_saus['sprinkels'] = hoeveelheid * SPINKELS

        elif topping == 'slagroom':
            gekozen_saus['slagroom'] = SLAGROOM

    return gekozen_saus

#particulere klant 
def bestelen_particuliere_klant(besteling: dict, smaken_kiez: list, gekozen_smaken: dict, gekozen_saus: dict):  
    while True:    
        try:
            hoeveelheid = input_check("Hoeveel bolletjes wilt u? ", int)
            
            if hoeveelheid <= 0:
                print(vout_melding)
                continue
            
            if hoeveelheid > MAX_BOLLETJES:
                print("Sorry, zulke grote bakken hebben we niet.")
                continue

            besteling['bolletjes'] += hoeveelheid
            
            gekozen_smaken = smaken_kies(hoeveelheid, smaken_kiez, gekozen_smaken)
            
            if 1 <= hoeveelheid <= 3:
                form_type = form_typ(hoeveelheid, besteling)
                saus(hoeveelheid, gekozen_saus, besteling)
                print(f"Hier is uw {form_type} met {hoeveelheid} bolletje(s).")
                break
            elif 4 <= hoeveelheid <= MAX_BOLLETJES:
                print(f"Dan krijgt u van mij een bakje met {hoeveelheid} bolletjes.")
                besteling['bakjes'] += 1
                saus(hoeveelheid, gekozen_saus, besteling)
                break
        except ValueError:
            print(vout_melding)


def rekening_particuliere_klant(besteling: dict, gekozen_smaken: dict, gekozen_saus: dict):
    clear_screen()
    totaal = (
        besteling['bolletjes'] * BOLLETJES +
        besteling['hoorentjes'] * HOORENTJES +
        besteling['bakjes'] * BAKJES +
        sum(gekozen_saus.values())
    )
    print(rekening_text)
    print('_'*len(rekening_text))
    print('')
    for smaak, aantal in gekozen_smaken.items():
        if aantal>0:
            smaak_str = f"{smaak.capitalize()} bolletje(s)"
            prijs = round(aantal * BOLLETJES, 2)
            print(f"{smaak_str:<20} {aantal:>2} x €{BOLLETJES:>5.2f} = €{prijs:6.2f}")
        
    if besteling['hoorentjes'] > 0:
        hoorn_prijs = round(besteling['hoorentjes'] * HOORENTJES, 2)
        print(f"Hoorntjes              {besteling['hoorentjes']:>2} x €{HOORENTJES:>5.2f} = €{hoorn_prijs:6.2f}")
    
    if besteling['bakjes'] > 0:
        bak_prijs = round(besteling['bakjes'] * BAKJES, 2)
        print(f"Bakjes                 {besteling['bakjes']:>2} x €{BAKJES:>5.2f} = €{bak_prijs:6.2f}")
    
    for topping, prijs in gekozen_saus.items():
        print(f"Toping                  = €{prijs:6.2f}")
    
    # Итог
    print("                         ----+")
    print(f"Totaal                 = €{totaal:6.2f}")

#zakelijke klant
def bestelen_zakelijke_klant(besteling):
        smak = input_check  ('Welke smak wilt u? ', str,['vanile','chocolad','aardbei','mint'])
        hoeveelheid = input_check('hoeveel litters wilt u van deze smak?', int)
        if hoeveelheid>0:
            if smak in besteling_zakelijke:
                besteling_zakelijke[smak] += hoeveelheid
            else:
                besteling_zakelijke[smak] = hoeveelheid
       
              
        
def rekening_zakijke(besteling):
    clear_screen()
    totaal = sum(besteling_zakelijke.values()) * LITER_IJS
    btw = round(totaal - (totaal / (1 + 9 / 100)), 2)

    print(rekening_text)
    for smaak, aantal in besteling_zakelijke.items():
        smaak_str = f'L.{smaak.capitalize()}'
        prijs = round(aantal * LITER_IJS, 2)
        
        print(f"{smaak_str:<20}{str(aantal):>5} x €{LITER_IJS:>5.2f} = €{prijs:6.2f}")
    print("                         ----+")
    print(f"Subtotaal              = €{totaal:6.2f}")
    print(f'BTW ({BTW}%)               = €{btw:6.2f}')
    print('-' * len(rekening_text))

