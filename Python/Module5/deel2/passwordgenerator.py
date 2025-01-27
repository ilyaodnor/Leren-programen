from random import choice
import string

SPECIALE_TEKENS = "@#$%&_?"
HOOFDLETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KLEINELETTERS = "abcdefghijklmnopqrstuvwxyz"
CIJFERS = "0123456789"

def kleinletters_tovoegen(string):
    a = sum(1 for i in string if i in KLEINELETTERS)
    return a >= 8

def hoofdletters_aantal(string):
    a = sum(1 for i in string if i in HOOFDLETTERS)
    return 1 <= a <= 6

def specialetekens_aantal(string):
    a = sum(1 for i in string if i in SPECIALE_TEKENS)
    return a == 3

def cijfers_aantal(string):
    a = sum(1 for i in string if i in CIJFERS) 
    return 4 <= a <= 7

def eerste_drie(string):
    return all(char not in CIJFERS for char in string[:3]) 

def hoofd_in_midden(string):
    if len(string) < 24: 
        return False
    return string[11] not in HOOFDLETTERS and string[12] not in HOOFDLETTERS

def passwordgenerator():
    while True:
        wachtwoord = ''.join(choice([choice(SPECIALE_TEKENS), choice(HOOFDLETTERS), 
                                     choice(KLEINELETTERS), choice(CIJFERS)]) for _ in range(24))
        if (kleinletters_tovoegen(wachtwoord) and hoofdletters_aantal(wachtwoord) and 
            specialetekens_aantal(wachtwoord) and cijfers_aantal(wachtwoord) and 
            eerste_drie(wachtwoord) and hoofd_in_midden(wachtwoord)):
            if wachtwoord[0]  in '@#$%&_?' or wachtwoord[-1] in '@#$%&_?':
                continue
            elif wachtwoord[-1] in string.ascii_lowercase:
                continue
            else:
                return wachtwoord
for i in range(50):
    print(passwordgenerator())