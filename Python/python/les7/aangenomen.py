leeftijd = 18 
snor = 'ja'
diploma = 'ja'
pers_leestijd = int(input('Hoe oud ben je?'))
pers_snor = input('Heb je een snor?')
pers_diploma = input('heb je diploma?')
if pers_leestijd >= leeftijd and pers_snor == snor or pers_diploma == diploma:
    print('Je  bent aangenomen!!')
else:
    print('je bent niet aangenomen')