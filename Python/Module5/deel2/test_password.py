from random import *
# password 24 karakters lang!
# Random 2 tot 6 hoofdletters.
# Een hoofdletter mag niet op de twee middelste posities staan.
## Minimaal 8 kleine letters.
## Het wachtwoord mag niet met een kleine letter eindigen.
# 3 speciale tekens uit de volgende reeks: @ # $ % & _ ?.
## De speciale tekens mogen niet op de eerste of laatste positie staan.
# Random 4 tot 7 cijfers (0 t/m 9).
## Op de eerste 3 posities mag geen cijfer staan
import time, string

def test_wachtwoord(ww) -> bool:
    if len(ww) < 24:
        print('te kort')
        return False
    if not 1 < len(list(filter(lambda a: a in string.ascii_uppercase, list(ww)))) < 7:
        print('aantal hoofdletters klopt niet!')
        return False
    if ww[11] in string.ascii_uppercase or ww[12] in string.ascii_uppercase:
        print('In het midden geen hoofdletters')
        return False
    if len(list(filter(lambda a: a in string.ascii_lowercase, list(ww)))) < 8:
        print('te weinig kleine letters')
        return False
    if ww[-1] in string.ascii_lowercase:
        print('Laatste pos niet juist')
        return False
    if len(list(filter(lambda a: a in '@#$%&_?', list(ww)))) != 3:
        print('te weinig specials')
        return False
    if ww[0] in '@#$%&_?' or ww[-1] in '@#$%&_?':
        print('special op end')
        return False
    if not 3 < len(list(filter(lambda a: a.isdigit(), list(ww)))) < 8:
        print('te weinig getallen')
        return False
    if ww[0].isdigit() or ww[1].isdigit() or ww[2].isdigit():
        print('Eerste drie karakters staat een getal')
        return False
    return True


    # plaats jouw code hier.

from random import choice


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
print(passwordgenerator())

for i in range(500):
    a = passwordgenerator()
    test_wachtwoord(a)
    print(a)
