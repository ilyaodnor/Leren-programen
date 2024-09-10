
leeftijd = int(input('Hoe oud ben je?'))
geen_toegang = not (leeftijd>= 18)
if  geen_toegang:
    print('Niet Welkom!')
else:
    print('Welkom!!')
