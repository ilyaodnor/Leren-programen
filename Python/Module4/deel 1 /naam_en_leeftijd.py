from functions import persoon
import os, termcolor
while True:
    personen_dict = persoon()
    vraag = input('wilt u nog een naam toevoegen?').lower()
    if vraag == 'ja':
        continue
    elif vraag == 'nee':
        break
os.system('clear')

for naam, details in personen_dict.items():
    if details['leeftijd'] <=18:
        print(f"In {termcolor.colored(details['woonplaats'], 'yellow')} woont {termcolor.colored(naam, 'green')}, die {termcolor.colored('nog niet', 'red')} volwassen is. ")
    else:
        print(f"In {termcolor.colored(details['woonplaats'], 'yellow')} woont {termcolor.colored(naam, 'green')}, die al {termcolor.colored('nog niet', 'red')} volwassen is. ")